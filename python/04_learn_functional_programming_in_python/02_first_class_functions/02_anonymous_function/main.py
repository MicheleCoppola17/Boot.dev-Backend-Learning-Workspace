"""
Assignment:
Complete the file_type_getter function. This function accepts a list of tuples, where each tuple contains:

1. A "file type" (e.g. "code", "document", "image", etc)
2. A list of associated file extensions (e.g. [".py", ".js"] or [".docx", ".doc"])

The function returns a function for looking up the file type of a given file extension.

1. Create an empty dictionary to map each file extension to its file type.
2. Loop through the file_extension_tuples:
    1. Loop through the file extensions.
    2. Add each extension to the dictionary and assign its value to the file type.

For example, if given the following list of tuples:

# list of tuples
[
    ("document", [".doc", ".docx"]),
    ("image", [".jpg", ".png"])
]

# resulting dictionary
{
    ".doc": "document",
    ".docx": "document",
    ".jpg": "image",
    ".png": "image",
}

3. Return a lambda function that accepts a string (a file extension) and returns its file type from the dictionary.
4. Use the .get dictionary method in the lambda function to return the file type of the extension if found or "Unknown" if it's missing.
"""

def file_type_getter(file_extension_tuples):
    extension_type = {}
    for file_type, extensions in file_extension_tuples:
        for extension in extensions:
            extension_type[extension] = file_type
    return lambda extension: extension_type.get(extension, "Unknown")

"""
# But also
def file_type_getter(file_extension_tuples):
    extension_type = {}
    for tup in file_extension_tuples:
        for extension in tup[1]:
            extension_type[extension] = tup[0]
    return lambda extension: extension_type.get(extension, "Unknown")
"""