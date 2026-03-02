"""
Assignment
Doc2Doc needs a feature that can take care of encoding characters as escape sequences in HTML documents.

You might not know anything about HTML. That's fine. This assignment isn't about HTML directly.

Just understand that it's a markup language like Markdown. Certain characters are interpreted as part of HTML syntax. In order to show these characters without interpreting them, they must be escaped, e.g., replace "<" with "&lt;".

Complete the replacer function.

1. It takes as input two strings, old and new, and returns a function, replace.
2. replace takes an input function, decorated_func, and returns a wrapper function.
3. wrapper takes as input a string text. It uses .replace() string method to replace instances of old with new in the text. Then it returns the result of passing the modified text to the decorated_func.
4. Use a series of the replacer function to decorate tag_pre. Pass the following pairs of strings to these decorators to encode the escape sequences:
    1. Replace "&" with "&amp;"
    2. Replace "<" with "&lt;"
    3. Replace ">" with "&gt;"
    4. Replace '"' with "&quot;"
    5. Replace "'" with "&#x27;"
"""

def replacer(old, new):
    def replace(decorate_func):
        def wrapper(text):
            text = text.replace(old, new)
            return decorate_func(text)
        return wrapper
    return replace


@replacer("&", "&amp;")
@replacer("<", "&lt;")
@replacer(">", "&gt;")
@replacer('"', "&quot;")
@replacer("'", "&#x27;")
def tag_pre(text):
    return f"<pre>{text}</pre>"
