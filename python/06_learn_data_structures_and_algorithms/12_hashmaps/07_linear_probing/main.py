"""
Assignment
Complete the insert and get methods.

Insert
1. Compute the index for the key in the hashmap with self.key_to_index(key). Create an original_index variable and assign index to it.
2. Initialize a boolean variable first_iteration to True.
3. Begin a while loop that continues as long as the hashmap's slot at index is occupied (not None) and its key doesn't match the key being inserted.
    - If this is not the first iteration and the current index equals original_index, raise an exception "hashmap is full". This means we've traversed the entire hashmap without finding an empty slot.
    - Increment index by 1 and wrap it around to the start of the hashmap if necessary (using modulo operation with hashmap's length).
    - Set first_iteration to False after the first iteration.
4. Insert the key-value pair at the found index: self.hashmap[index] = (key, value).

Get
1. Compute the index for the key in the hashmap with self.key_to_index(key). Create an original_index variable and assign index to it.
2. Initialize a boolean variable first_iteration to True.
3. Begin a while loop that continues as long as the hashmap's slot at index is occupied (not None).
    - If the key at the current index matches the key being searched, return the value from the key-value pair in the hashmap at the current index.
    - If this is not the first iteration and the current index equals original_index, raise an exception "sorry, key not found". This means we've traversed the entire hashmap without finding the key.
    - If the key does not match, increment index by 1 and wrap it around to the start of the hashmap if necessary (using modulo operation with hashmap's length).
    - Set first_iteration to False after the first iteration.
4. If the while loop completes without finding a match, raise an exception "sorry, key not found".
"""

from typing import Any


class HashMap:
    def insert(self, key: str, value: Any) -> None:
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True
        while self.hashmap[index] is not None and self.hashmap[index][0] != key:
            if not first_iteration and index == original_index:
                raise Exception("hashmap is full")
            index = (index + 1) % len(self.hashmap)
            first_iteration = False
        self.hashmap[index] = (key, value)

    def get(self, key: str) -> Any:
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True
        while self.hashmap[index] is not None:
            if self.hashmap[index][0] == key:
                return self.hashmap[index][1]
            elif not first_iteration and index == original_index:
                raise Exception("sorry, key not found")
            else:
                index = (index + 1) % len(self.hashmap)
            first_iteration = False
        raise Exception("sorry, key not found")

    # don't touch below this line

    def __init__(self, size: int) -> None:
        self.hashmap: list[tuple[str, Any] | None] = [None for i in range(size)]

    def key_to_index(self, key: str) -> int:
        total = 0
        for c in key:
            total += ord(c)
        return total % len(self.hashmap)

    def __repr__(self) -> str:
        final = ""
        for i, v in enumerate(self.hashmap):
            if v is not None:
                final += f" - {str(v)}\n"
        return final
