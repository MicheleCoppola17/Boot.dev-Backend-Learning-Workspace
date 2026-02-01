"""
Assignment:
Our Doc2Doc utility is designed to accept input documents in a variety of formats. It chooses the appropriate parser for a document based on the extension of the file name. Currently, only Markdown and plain-text parsers are supported.

Fix the choose_parser function. The logic is correct, but we want to simplify the conditional block to a one-line ternary expression.
"""
"""
# Initial function
def choose_parser(file_extension):
    if file_extension.lower() in ("markdown", "md"):
        return "markdown"
    else:
        return "plaintext"
"""

def choose_parser(file_extension):
    return "markdown" if file_extension.lower() in ("markdown", "md") else "plaintext"
