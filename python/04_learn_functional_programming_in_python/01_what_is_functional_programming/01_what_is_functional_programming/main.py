"""
Assignment:
Complete the stylize_title function. It should take a single string as input, and return a single string as output. The returned string should have both the title centered and a border added.

- Use the provided functions center_title and add_border.
- Center the title before adding the border.
- Do not create any variables.
- Use only 1 line of code in the function body.
"""

def stylize_title(document):
    return add_border(center_title(document))


# Don't touch below this line


def center_title(document):
    width = 40
    title = document.split("\n")[0]
    centered_title = title.center(width)
    return document.replace(title, centered_title)


def add_border(document):
    title = document.split("\n")[0]
    border = "*" * len(title)
    return document.replace(title, title + "\n" + border)
