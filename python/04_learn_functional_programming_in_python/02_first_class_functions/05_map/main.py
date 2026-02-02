"""
Assignment:
Markdown supports two different styles of bullet points, - and *. We prefer *, so, we need a function to convert any - bullet points to * bullet points.

Complete the change_bullet_style function. It takes a document (a string) as input, and returns a single string as output. The returned string should have any lines that start with a - character replaced with a * character.

For example, this:

- This is a bullet
- This is a bullet

Becomes:

* This is a bullet
* This is a bullet

Use the built-in map function to apply the provided convert_line function to each line of the input string. Use .split() and .join() to split the document into a list of lines, and then join the lines back together. This should preserve the original line breaks. Don't use the .replace() string method.

Examples of split and join:

# my_document is a string with newlines
lines_list = my_document.split("\n")

rejoined_doc = "\n".join(lines_list)
"""

def change_bullet_style(document):
    splitted = document.split("\n")
    converted = map(convert_line, splitted)
    joined = "\n".join(converted)
    return joined


# Don't edit below this line


def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
