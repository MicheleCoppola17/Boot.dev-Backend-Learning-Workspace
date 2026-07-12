"""
Assignment
We're going to use a trie to add "prefix searching" to LockedIn. 
For example, a user will be able to type "dev" into a job search bar and see the autocomplete suggestions "developer", "development", "devops", etc.

Complete the add method. It takes a word as input, and should add it to the trie.

1. Keep track of your "current level" in the trie, starting at the root.
2. Loop over each character in the word-to-add:
    1. If the character is not a key in the current level, add it and create a new nested level (dictionary) for it.
    2. Outside the if statement, update your "current level" to the nested dictionary for this character (whether it was just created or already existed).
3. Once you've ensured all the dictionaries exist, add an entry to the dictionary of the last character in the word with self.end_symbol as the key and True as the value. This will indicate that this is a complete word and not just a prefix of another word.
"""

from typing import Any


class Trie:
    def add(self, word: str) -> None:
        current_level = self.root

        for letter in word:
            if letter not in current_level:
                current_level[letter] = {}
            current_level = current_level[letter]
            
        current_level[self.end_symbol] = True

    # don't touch below this line

    def __init__(self) -> None:
        self.root: dict[str, Any] = {}
        self.end_symbol = "*"
