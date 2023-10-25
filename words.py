def print_upper_words(words):
    """Converst a list of words to uppercase"""
    for word in words:
        print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])

def print_upper_words2(words):
    """Converts a list of words to uppercase"""
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

    return

print_upper_words2(["eyelash", "hello", "hey", "goodbye", "yo", "yes"])

def print_upper_words(words, letters):
    """Converst a list of words to uppercase"""
    
    for word in words:
        for letter in letters:
            if word.startswith(letter):
                print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], ["h", "y"])