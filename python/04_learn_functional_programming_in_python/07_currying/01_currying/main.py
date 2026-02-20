"""
Assignment
In Doc2Doc, for some types of text files, we need to transform the font size of the text when rendering it onscreen.

Fix the converted_font_size function. We are using a 3rd party code library that expects our function to be a curried series of functions that each take a single argument.

- converted_font_size should just take a single argument, font_size and return a new function.
- The returned function should take a single argument, doc_type, and return font_size multiplied by the appropriate value for the given doc_type.
"""

def converted_font_size(font_size):
    def conversion(doc_type):
        if doc_type == "txt":
            return font_size
        if doc_type == "md":
            return font_size * 2
        if doc_type == "docx":
            return font_size * 3
        raise ValueError("invalid doc type")
    return conversion
