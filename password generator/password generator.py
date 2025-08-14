import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Characters sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one character from each set
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password
    all_chars = letters + digits + symbols
    password += [random.choice(all_chars) for _ in range(length - 3)]

    # Shuffle to avoid predictable pattern
    random.shuffle(password)

    return "".join(password)

# User input
length = int(input("Enter password length: "))
print("Generated Password:", generate_password(length))
