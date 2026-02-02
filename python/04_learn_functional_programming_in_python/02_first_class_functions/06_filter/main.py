"""
Assignment:
Complete the remove_invalid_lines function. It accepts a document string as input. It should:

1. Use the built-in filter function with a lambda to make a filtered copy of the input document.
    1. Remove any lines that start with a - character.
    2. Keep all other lines and preserve any trailing newlines (\n).
2. Return the result, all on one expression.

For example, this:

* Star Wars episode 1 is underrated
- Star Wars episode 9 is fine
* Star Wars episode 3 is the best


Should become:

* Star Wars episode 1 is underrated
* Star Wars episode 3 is the best
"""

def remove_invalid_lines(document):
    return "\n".join(
        filter(lambda line: not line.startswith("-"), document.split("\n"))
    )

