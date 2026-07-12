"""
Assignment
Complete the advanced_find_matches method. 
It takes an entire document and a dictionary of character variations as input, and should return a set() of all the words in the trie that exist in the document as continuous substrings, even if the word had a variation character instead of the original.

For example, if:

- The document contains "d@rn"
- The variations dictionary contains {'@': 'a'}
- "darn" is in the trie

...then "d@rn" should be returned as a match.
"""

from typing import Any


class Trie:
    def advanced_find_matches(
        self, document: str, variations: dict[str, str]
    ) -> set[str]:
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                normalized_ch = variations.get(ch, ch)
                if normalized_ch not in level:
                    break
                level = level[normalized_ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches

    # don't touch below this line

    def find_matches(self, document: str) -> set[str]:
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches

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
