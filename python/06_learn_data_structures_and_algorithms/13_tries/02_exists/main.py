"""
Assignment
We want to be able to see what words have been added to the trie.

Complete the exists method. It takes a word as input, and should return True if the word exists in the trie, and False if it doesn't.

1. Starting with the root of the trie, assign the current dictionary to a variable.
2. Loop over the letters in the word.
    1. If the current letter is not in the current dictionary, return False.
    2. Update current to point to the dictionary at the letter key.
3. Once you get to the last letter, return True if end_symbol is in the current dictionary, and False if it isn't.
"""

from typing import Any


class Trie:
    def exists(self, word: str) -> bool:
        current_dict = self.root
        
        for letter in word:
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        
        return self.end_symbol in current_dict
    # don't touch below this line

    def add(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def __init__(self) -> None:
        self.root: dict[str, Any] = {}
        self.end_symbol = "*"
