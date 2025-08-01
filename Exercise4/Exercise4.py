# Kunal Sharma IIT Jammu
# Exercise 4: Enhanced Secret Code Language Translator
# This program encodes and decodes messages using a secret Algo.
import random
import string


def generate_random_chars(n=3):
    return "".join(random.choices(string.ascii_letters + string.digits, k=n))


def shift_characters(word, offset=3):
    shifted_word = "".join(
        (
            chr((ord(char) - ord("a") + offset) % 26 + ord("a"))
            if char.islower()
            else (
                chr((ord(char) - ord("A") + offset) % 26 + ord("A"))
                if char.isupper()
                else char
            )
        )
        for char in word
    )
    return shifted_word


def encode_word(word):
    if len(word) >= 3:
        reversed_word = word[::-1]
        shifted_word = shift_characters(reversed_word, offset=5)
        random_start = generate_random_chars(4)
        random_end = generate_random_chars(4)
        return random_start + shifted_word + random_end
    else:
        return shift_characters(word[::-1], offset=5)


def decode_word(word):
    if len(word) < 3:
        return shift_characters(word[::-1], offset=-5)
    else:
        core_word = word[4:-4]
        unshifted_word = shift_characters(core_word, offset=-5)
        return unshifted_word[::-1]


def encode_message(message):
    words = message.split()
    encoded_words = [encode_word(word) for word in words]
    encoded_message = "".join(
        f"{len(word)}{encoded_word}" for word, encoded_word in zip(words, encoded_words)
    )
    return encoded_message


def decode_message(message):
    decoded_words = []
    i = 0
    while i < len(message):
        word_length = int(message[i])
        i += 1
        encoded_word = message[i : i + word_length + 8]
        i += word_length + 8
        decoded_words.append(decode_word(encoded_word))
    return " ".join(decoded_words)


def main():
    print("Enhanced Secret Code Language Translator")
    print("1. Encode a message")
    print("2. Decode a message")

    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        message = input("Enter the message to encode: ").strip()
        encoded = encode_message(message)
        print(f"Encoded message: {encoded}")
    elif choice == "2":
        message = input("Enter the message to decode: ").strip()
        decoded = decode_message(message)
        print(f"Decoded message: {decoded}")
    else:
        print("Invalid choice! Please enter 1 or 2.")


if __name__ == "__main__":
    main()
