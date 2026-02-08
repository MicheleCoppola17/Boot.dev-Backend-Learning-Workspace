"""
Assignment
Fix the remove_emphasis function by making it pure.

remove_emphasis takes a document with any number of lines and removes any number of * characters that are at the start or end of a word. (In case you need it, here's a primer on emphasis in Markdown.)

For example, this:

I *love* Markdown.
I **really love** Markdown.
I ***really really love*** Markdown.

Should become:

I love Markdown.
I really love Markdown.
I really really love Markdown.

The problem is that remove_emphasis is currently impure - it modifies a global variable called doc. It should instead accept a document as an argument and return a new document with emphasis removed.

Once you've purified remove_emphasis, you can also delete the global doc variable.

The functions in this assignment use some Python built-ins that are definitely worth knowing, including str.split, str.strip, map, and join.
"""

doc = """I *love* Markdown.
I **really love** Markdown.
I ***really really love*** Markdown."""

"""
def remove_emphasis():
    global doc
    lines = doc.split("\n")
    new_lines = map(remove_line_emphasis, lines)
    doc = "\n".join(new_lines)
"""

# My solution
def remove_emphasis(doc):
    lines = doc.split("\n")
    new_lines = map(remove_line_emphasis, lines)
    return "\n".join(new_lines)

# Don't touch below this line


def remove_line_emphasis(line):
    words = line.split()
    new_words = map(remove_word_emphasis, words)
    return " ".join(new_words)


def remove_word_emphasis(word):
    return word.strip("*")
