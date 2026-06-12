"""
Assignment
Complete the letter_combinations function using the algorithm outlined below. It takes a string of digits and returns a list of strings of letters.

1. If the input string is empty, return an empty list.
2. Define a result list to hold the output strings. Have it contain just an empty string to start (we need that one element to build on).
3. Iterate over the input digits. For each of them:
    1. If the digit is any invalid character, i.e. not found in the provided digit_to_letters dictionary, raise a ValueError to abort the function:
        
        raise ValueError(f"invalid digit: {digit}")

    2. Get the string of letters that can be represented by the current digit, from digit_to_letters.
    3. Define a new_result list - empty to start with.
    4. Enter two nested for loops:
        - For each existing letter combo in result, iterate over each letter in the current digit's letters.
        - Append combo + letter to new_result.
    5. After the two nested loops, but still inside the main loop over digits, set result equal to new_result.
4. After the main loop, return the result.
"""

def letter_combinations(digits: str) -> list[str]:
    if len(digits) == 0:
        return []
    result = [""]
    for digit in digits:
        if digit not in digit_to_letters:
            raise ValueError(f"invalid digit: {digit}")
        letters = digit_to_letters[digit]
        new_result = []
        for combo in result:
            for letter in letters:
                new_result.append(combo + letter)
        result = new_result
    return result
        


# Don't touch below this line

digit_to_letters = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}
