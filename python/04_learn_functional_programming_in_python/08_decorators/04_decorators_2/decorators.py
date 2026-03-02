"""
Assignment
Complete the markdown_to_text_decorator function. It can decorate a function with any number of string arguments, no matter if they're positional or keyword args. It will run the decorated function, but first strip out any Markdown heading symbols (see below for an explanation of Markdown headings).

It should return a wrapper function that takes *args and **kwargs. The wrapper should:

1. Map the *args to a new list where each string is converted to plain text using convert_md_to_txt.
2. Map the **kwargs to a new dictionary where each "value" is converted to plain text using convert_md_to_txt. The "key" should remain the same.
    - Use the .items() dictionary method to pass a list of tuples of key-value pairs to map
    - Create a function for map which changes the value of an item tuple with convert_md_to_txt
3. Return the result of calling the decorated function with the new arguments.
"""

def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        converted_args = map(convert_md_to_txt, args)
        converted_kwargs = dict(map(map_kwargs, kwargs.items()))

        return func(*converted_args, **converted_kwargs)

    return wrapper

def map_kwargs(kwargs_tuple):
    return (kwargs_tuple[0], convert_md_to_txt(kwargs_tuple[1]))


# don't touch below this line


def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)
