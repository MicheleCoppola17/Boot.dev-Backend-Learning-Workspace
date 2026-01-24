"""
Assignment:
Complete the count_vowels function. It takes a string and returns:

1. The total number of vowels in the string (count every occurrence, not just unique)
2. A set of the unique vowels found in the string

We are only interested in the 5 vowels: a, e, i, o, u, and their capitalized versions. 
Treat uppercase and lowercase vowels as separate. For example, "A" and "a" are not the same.
"""

def count_vowels(text):
    existing_vowels = {"a", "e","i", "o", "u", "A", "E", "I", "O", "U"}
    unique_vowels = set()

    vowel_counter = 0

    for letter in text:
        if letter in existing_vowels:
            unique_vowels.add(letter)
            vowel_counter += 1

    return vowel_counter, unique_vowels
