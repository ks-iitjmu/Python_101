import random
import string

def generate_random_chars(n=3):
    """Generate n random characters"""
    return ''.join(random.choices(string.ascii_lowercase, k=n))

def encode_word(word):
    """Encode a single word using the secret code rules"""
    if len(word) >= 3:
        # Remove first letter and append at end
        modified_word = word[1:] + word[0]
        # Add 3 random characters at start and end
        random_start = generate_random_chars(3)
        random_end = generate_random_chars(3)
        return random_start + modified_word + random_end
    else:
        # Simply reverse the string
        return word[::-1]

def decode_word(word):
    """Decode a single word using the secret code rules"""
    if len(word) < 3:
        # Reverse it
        return word[::-1]
    else:
        # Remove 3 characters from start and end
        core_word = word[3:-3]
        # Remove last letter and append to beginning
        if len(core_word) > 0:
            return core_word[-1] + core_word[:-1]
        return core_word

def encode_message(message):
    """Encode entire message"""
    words = message.split()
    encoded_words = [encode_word(word) for word in words]
    return ' '.join(encoded_words)

def decode_message(message):
    """Decode entire message"""
    words = message.split()
    decoded_words = [decode_word(word) for word in words]
    return ' '.join(decoded_words)

def main():
    print("Secret Code Language Translator")
    print("1. Encode a message")
    print("2. Decode a message")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == '1':
        message = input("Enter the message to encode: ").strip()
        encoded = encode_message(message)
        print(f"Encoded message: {encoded}")
    elif choice == '2':
        message = input("Enter the message to decode: ").strip()
        decoded = decode_message(message)
        print(f"Decoded message: {decoded}")
    else:
        print("Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()