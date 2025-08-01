# Python 101 - Learning Python Programming

A comprehensive collection of Python programming exercises and projects designed for beginners to learn fundamental programming concepts and practice coding skills.

## 📋 Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Exercises](#exercises)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## 🎯 Overview

This repository contains a series of Python programming exercises that cover basic to intermediate concepts. Each exercise is designed to teach specific programming fundamentals while building practical coding skills.

## 📁 Project Structure

```
Python_101/
├── main.ipynb              # Jupyter notebook with Python exercises and examples
├── example.txt             # Sample text file
├── LICENSE                 # MIT License
├── README.md              # Project documentation
├── Exercise1/
│   └── Exercise1.py       # Simple Calculator Program
├── Exercise2/
│   └── Exercise2.py       # Time-based Greeting Program
├── Exercise3/
│   ├── Exercise3.py       # KBC (Kaun Banega Crorepati) Game
│   ├── easyQues.json      # Easy difficulty questions
│   ├── mediumQues.json    # Medium difficulty questions
│   └── hardQues.json      # Hard difficulty questions
└── Exercise4/
    └── Exercise4.py       # Secret Code Language Translator
```

## 🚀 Exercises

### Exercise 1: Simple Calculator
**File:** `Exercise1/Exercise1.py`

A basic calculator program that performs arithmetic operations:
- Addition, Subtraction, Multiplication, Division
- Error handling for division by zero
- Input validation for numeric values

**Features:**
- Menu-driven interface
- Exception handling
- User-friendly error messages

### Exercise 2: Time-based Greeting
**File:** `Exercise2/Exercise2.py`

A program that displays different greetings based on the current time:
- Good morning (5 AM - 12 PM)
- Good afternoon (12 PM - 5 PM)
- Good evening (5 PM - 9 PM)
- Good night (9 PM - 5 AM)

**Concepts covered:**
- Time module usage
- Conditional statements
- System time handling

### Exercise 3: KBC Game (Kaun Banega Crorepati)
**File:** `Exercise3/Exercise3.py`

A complete quiz game implementation inspired by the popular Indian game show:
- Multiple difficulty levels (Easy, Medium, Hard)
- 15 questions with increasing prize money
- 4 lifelines: 50-50, Audience Poll, Phone a Friend, Ask the Expert
- Safe havens at certain levels
- JSON-based question database

**Features:**
- Object-oriented programming
- File I/O operations
- JSON data handling
- Game state management
- Interactive user interface

**Question Database:**
- `easyQues.json` - Easy level questions
- `mediumQues.json` - Medium level questions  
- `hardQues.json` - Hard level questions

### Exercise 4: Secret Code Language Translator
**File:** `Exercise4/Exercise4.py`

A program that encodes and decodes messages using a secret algorithm:

**Encoding Rules:**
- Words ≥ 3 characters: Move first letter to end + add 3 random chars at start and end
- Words < 3 characters: Simply reverse the string

**Decoding Rules:**
- Reverse of encoding process
- Remove random characters and restore original word structure

**Features:**
- String manipulation
- Random character generation
- Bidirectional encoding/decoding
- Message processing

## 🛠️ Getting Started

### Prerequisites

- Python 3.7 or higher
- Jupyter Notebook (optional, for `main.ipynb`)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ks-iitjmu/Python_101.git
   cd Python_101
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install jupyter  # Only if you want to run the notebook
   ```

## 💻 Usage

### Running Individual Exercises

**Exercise 1 - Calculator:**
```bash
cd Exercise1
python Exercise1.py
```

**Exercise 2 - Time Greeting:**
```bash
cd Exercise2
python Exercise2.py
```

**Exercise 3 - KBC Game:**
```bash
cd Exercise3
python Exercise3.py
```

**Exercise 4 - Secret Code Translator:**
```bash
cd Exercise4
python Exercise4.py
```

### Running the Jupyter Notebook

```bash
jupyter notebook main.ipynb
```

## 🎮 Game Instructions

### KBC Game (Exercise 3)
1. Answer 15 multiple-choice questions
2. Each correct answer increases your prize money
3. Use lifelines strategically:
   - **50-50**: Eliminates two wrong options
   - **Audience Poll**: Shows percentage vote for each option
   - **Phone a Friend**: Get a friend's suggestion
   - **Ask the Expert**: Get expert advice
4. Safe havens: ₹10,000, ₹3,20,000, and ₹1,00,00,000
5. Win up to ₹1 Crore!

### Secret Code Translator (Exercise 4)
1. Choose to encode or decode a message
2. Enter your message
3. Get the transformed result
4. Use the opposite operation to verify

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-exercise`)
3. Add your exercise or improvement
4. Commit your changes (`git commit -am 'Add new exercise'`)
5. Push to the branch (`git push origin feature/new-exercise`)
6. Create a Pull Request

### Guidelines for new exercises:
- Follow the existing code structure
- Include comprehensive comments
- Add error handling where appropriate
- Create a brief description in this README

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Kunal Sharma**  
IIT Jammu

---

## 🎯 Learning Outcomes

By completing these exercises, you will learn:

- **Basic Python Syntax**: Variables, data types, operators
- **Control Structures**: If-else statements, loops
- **Functions**: Definition, parameters, return values
- **Error Handling**: Try-catch blocks, exception handling
- **File Operations**: Reading from and writing to files
- **JSON Handling**: Parsing and manipulating JSON data
- **Object-Oriented Programming**: Classes, objects, methods
- **String Manipulation**: Processing and transforming text
- **Time Handling**: Working with system time and dates
- **User Interface**: Creating interactive console applications

## 🔧 Troubleshooting

**Common Issues:**

1. **JSON file not found (Exercise 3):**
   - Ensure you're running the script from the Exercise3 directory
   - Check that all JSON files are present

2. **Module import errors:**
   - Make sure you're using Python 3.7+
   - Install required packages if any are missing

3. **Encoding issues:**
   - Ensure your terminal supports UTF-8 encoding for special characters

---

Happy coding! 🐍✨