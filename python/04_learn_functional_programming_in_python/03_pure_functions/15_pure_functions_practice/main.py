"""
Assignment
Fix the following issues to make the functions pure:

1. add_custom_command is mutating an input
2. add_format is mutating an input
3. save_document is mutating an input
4. add_line_break has a side effect (printing to stdout) and no return value
"""

default_commands = {}
default_formats = ["txt", "md", "html"]
saved_documents = {}

# Don't edit above this line


def add_custom_command(commands, new_command, function):
    new_commands = commands.copy()
    new_commands[new_command] = function
    return new_commands


def add_format(formats, format):
    new_formats = formats.copy()
    new_formats.append(format)
    return new_formats


def save_document(docs, file_name, doc):
    new_docs = docs.copy()
    new_docs[file_name] = doc
    return new_docs


def add_line_break(line):
    return line + "\n\n"