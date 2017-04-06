ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def is_pangram(text):
    for char in ALPHABET:
        if char not in text.lower():
            return False
    return True