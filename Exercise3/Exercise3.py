import random
import time
import json
import os
from typing import List, Dict, Optional, Tuple

class KBCGame:
    def __init__(self):
        self.prizes = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 
                      160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
        self.safe_havens = [10000, 320000, 10000000]
        self.lifelines = {
            "50-50": True,
            "Audience Poll": True,
            "Phone a Friend": True,
            "Ask the Expert": True
        }
        self.questions = self._load_questions()
        self.score = 0

    def _load_questions(self) -> List[Dict]:
        """Load questions from JSON files"""
        all_questions = []
        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        files = ['easyQues.json', 'mediumQues.json', 'hardQues.json']
        
        for file in files:
            file_path = os.path.join(script_dir, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    questions_data = json.load(f)
                    all_questions.extend(questions_data)
            except FileNotFoundError:
                print(f"Warning: {file} not found. Skipping...")
            except json.JSONDecodeError:
                print(f"Error: Invalid JSON in {file}. Skipping...")
        
        if not all_questions:
            raise ValueError("No questions found! Please check your JSON files.")
        
        return all_questions

    @staticmethod
    def clear_console():
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def display_header():
        """Display game header"""
        print("=" * 60)
        print("   🎯 KON BANEGA CROREPATI - 2024 EDITION 🎯")
        print("=" * 60)
        print()

    def show_prize_ladder(self, current_level: int):
        """Display the prize ladder"""
        print("\n💰 PRIZE LADDER:")
        print("-" * 40)
        for i, prize in enumerate(reversed(self.prizes)):
            level = len(self.prizes) - i
            marker = "👉" if level == current_level + 1 else "  "
            safe_marker = "🛡️ " if prize in self.safe_havens else "   "
            print(f"{marker} {safe_marker}Q{level:2d}: Rs. {prize:,}")
        print("-" * 40)

    def _use_5050(self, question: Dict) -> List[str]:
        """Implement 50-50 lifeline"""
        correct = question["answer"]
        options = ["A", "B", "C", "D"]
        options.remove(correct)
        removed = random.sample(options, 2)
        
        new_options = [opt for opt in question["options"] 
                      if opt[0] == correct or opt[0] not in removed]
        
        print("🔄 50-50 Lifeline Used! Two wrong answers removed.")
        return new_options

    def _use_audience_poll(self, question: Dict):
        """Implement audience poll lifeline"""
        correct = question["answer"]
        
        # Base random distribution
        poll = {opt: random.randint(15, 35) for opt in ["A", "B", "C", "D"]}
        
        # Adjust correct answer based on difficulty
        difficulty_bonus = {
            "easy": random.randint(30, 50),
            "medium": random.randint(20, 40),
            "hard": random.randint(10, 30)
        }
        poll[correct] += difficulty_bonus.get(question.get("level", "medium"), 25)
        
        total = sum(poll.values())
        print("\n📊 AUDIENCE POLL RESULTS:")
        print("-" * 25)
        for opt in ["A", "B", "C", "D"]:
            percent = int(poll[opt] * 100 / total)
            bar = "█" * (percent // 5)
            print(f"{opt}: {percent:2d}% {bar}")
        print("-" * 25)

    def _use_phone_friend(self, question: Dict):
        """Implement phone a friend lifeline"""
        correct = question["answer"]
        friends = ["Rahul", "Priya", "Amit", "Sneha", "Vikash"]
        friend = random.choice(friends)
        
        print(f"\n📞 Calling your friend {friend}...")
        time.sleep(2)
        print(f"{friend}: Hello! Let me think...")
        time.sleep(1)
        
        confidence = (random.randint(60, 90) if question.get("level") == "easy" 
                     else random.randint(40, 70))
        
        if random.randint(1, 100) <= confidence:
            print(f"{friend}: I'm {confidence}% sure the answer is {correct}.")
        else:
            wrong_answers = [opt for opt in ["A", "B", "C", "D"] if opt != correct]
            suggested = random.choice(wrong_answers)
            print(f"{friend}: I think it might be {suggested}, but I'm not very sure.")

    def _use_ask_expert(self, question: Dict):
        """Implement ask the expert lifeline"""
        correct = question["answer"]
        expert_name = "Dr. Sharma"
        
        print(f"\n🎓 Asking the expert {expert_name}...")
        time.sleep(2)
        
        if random.randint(1, 100) <= 85:
            print(f"{expert_name}: Based on my knowledge, the answer is {correct}.")
        else:
            print(f"{expert_name}: This is tricky, but I believe it's {correct}.")

    def _handle_lifeline(self, question: Dict, lifelines_copy: Dict, 
                        available_lifelines: List[str]) -> List[str]:
        """Handle lifeline usage"""
        print("\nAvailable lifelines:")
        for i, lifeline in enumerate(available_lifelines, 1):
            print(f"{i}. {lifeline}")
        
        try:
            choice = int(input("Choose lifeline (number): ")) - 1
            if 0 <= choice < len(available_lifelines):
                lifeline = available_lifelines[choice]
                
                lifeline_actions = {
                    "50-50": lambda: self._use_5050(question),
                    "Audience Poll": lambda: (self._use_audience_poll(question), question["options"])[1],
                    "Phone a Friend": lambda: (self._use_phone_friend(question), question["options"])[1],
                    "Ask the Expert": lambda: (self._use_ask_expert(question), question["options"])[1]
                }
                
                result = lifeline_actions[lifeline]()
                lifelines_copy[lifeline] = False
                
                return result if lifeline == "50-50" else question["options"]
            else:
                print("Invalid choice!")
                return question["options"]
        except ValueError:
            print("Invalid input!")
            return question["options"]

    def ask_question(self, question: Dict, question_num: int) -> Optional[bool]:
        """Ask a single question and handle user input"""
        lifelines_copy = self.lifelines.copy()
        current_options = question["options"][:]
        
        while True:
            self.clear_console()
            self.display_header()
            self.show_prize_ladder(question_num - 1)
            
            print(f"\n🎯 QUESTION {question_num} for Rs. {self.prizes[question_num-1]:,}")
            print("-" * 50)
            print(f"📝 {question['question']}")
            print()
            
            for option in current_options:
                print(f"   {option}")
            print()
            
            available_lifelines = [k for k, v in lifelines_copy.items() if v]
            if available_lifelines:
                print(f"💡 Available lifelines: {', '.join(available_lifelines)}")
                print("   Type 'lifeline' to use a lifeline")
            
            print("   Type 'quit' to quit the game")
            answer = input("\n🎤 Your answer (A/B/C/D): ").strip().upper()
            
            if answer == "LIFELINE" and available_lifelines:
                current_options = self._handle_lifeline(question, lifelines_copy, available_lifelines)
                input("\nPress Enter to continue...")
                continue
                
            elif answer in ["A", "B", "C", "D"]:
                return answer == question["answer"]
            elif answer == "QUIT":
                return None
            else:
                print("❌ Invalid input. Please enter A, B, C, D, 'lifeline', or 'quit'")
                time.sleep(1)

    def get_safe_amount(self) -> int:
        """Calculate safe amount based on current score"""
        safe_amount = 0
        for safe in reversed(self.safe_havens):
            if self.score > 0 and self.prizes[self.score-1] >= safe:
                safe_amount = safe
                break
        return safe_amount

    def play_game(self):
        """Main game loop"""
        self.clear_console()
        self.display_header()
        
        print("🎊 Welcome to Kon Banega Crorepati 2024!")
        print("Answer 15 questions correctly to win Rs. 1 Crore!")
        print(f"Safe havens are at: Rs. {', Rs. '.join(map(str, self.safe_havens))}")
        
        input("\nPress Enter to start the game...")
        
        if len(self.questions) < 15:
            print(f"Warning: Only {len(self.questions)} questions available!")
        
        selected_questions = random.sample(self.questions, min(15, len(self.questions)))
        
        for question in selected_questions:
            result = self.ask_question(question.copy(), self.score + 1)
            
            if result is None:  # Quit
                safe_amount = self.get_safe_amount()
                self.clear_console()
                self.display_header()
                print(f"\n🚪 You quit the game!")
                print(f"💰 You take home: Rs. {safe_amount:,}")
                break
                
            elif result:  # Correct answer
                print("✅ Correct Answer!")
                self.score += 1
                
                if self.score == len(selected_questions):
                    self.clear_console()
                    self.display_header()
                    print("\n🎊🎊 CONGRATULATIONS! 🎊🎊")
                    print(f"🏆 You are the CROREPATI! You won Rs. {self.prizes[self.score-1]:,}!")
                    break
                else:
                    print(f"💰 You have won Rs. {self.prizes[self.score-1]:,}")
                    input("\nPress Enter to continue to the next question...")
                    
            else:  # Wrong answer
                print(f"❌ Wrong Answer! The correct answer was {question['answer']}")
                safe_amount = self.get_safe_amount()
                input("\nPress Enter to see final results...")
                self.clear_console()
                self.display_header()
                print(f"💰 You take home: Rs. {safe_amount:,}")
                break
        
        print("\n🎯 Thank you for playing Kon Banega Crorepati!")
        print("=" * 60)

def main():
    try:
        game = KBCGame()
        game.play_game()
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\n\nGame interrupted by user. Goodbye!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
