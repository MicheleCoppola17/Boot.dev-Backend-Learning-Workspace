"""
Assignment
Complete the longest_common_prefix method. It returns the longest common prefix among the words in the trie.

1. Initialize a variable current that references the root of the trie
2. Initialize a variable prefix to an empty string
3. Enter a forever while loop:
    1. Create an empty children list.
    2. Iterate over the keys of current. Append each key that isn't the end_symbol to children.
    3. If the end_symbol is in current, or there isn't exactly one child, break the loop.
    4. Otherwise, append the single child character to the prefix string and update current to point to that child's dictionary.
4. Return the prefix string.
"""

from typing import Any


class Trie:
    def longest_common_prefix(self) -> str:
        current = self.root
        prefix = ""

        while True:
            children = []

            for key in current:
                if key != self.end_symbol:
                    children.append(key)
            if self.end_symbol in current or len(children) != 1:
                break
            else:
                prefix += children[0]
                current = current[children[0]]
        return prefix

    # don't touch below this line

    def __init__(self) -> None:
        self.root: dict[str, Any] = {}
        self.end_symbol = "*"

    def add(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True
