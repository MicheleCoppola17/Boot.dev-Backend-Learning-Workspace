"""
Assignment
Complete the convert_format function. Using the enum DocFormat, it should support 3 types of conversions:

1. From MD to HTML:
- Assume the content is a single h1 tag in markdown syntax - it's a single string representing a line. Replace the leading # with an <h1> and add a </h1> to the end.
- # This is a heading -> <h1>This is a heading</h1>
2. From TXT to PDF:
- Simply add a [PDF] tag to the beginning and end of the content. Notice the spaces between [PDF] tags and the content:
- This is some text -> [PDF] This is some text [PDF]
3. From HTML to MD:
- Replace any <h1> tags with # and remove any </h1> tags.
- <h1>This is a heading</h1> -> # This is a heading
4. Any other conversion:
- If the input format is invalid, raise an Exception with the string invalid type.
"""

from enum import Enum

DocFormat = Enum("DocFormat", ["PDF", "TXT", "MD", "HTML"])

# don't touch above this line


def convert_format(content, from_format, to_format):
    pass
