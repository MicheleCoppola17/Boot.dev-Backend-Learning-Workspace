"""
Assignment
We have a way for Doc2Doc users to set their supported formats in their settings. In memory, we store those settings as a simple dictionary:

settings = {
    "docx": True,
    "pdf": True,
    "txt": False
}

Unfortunately, there is a bug in our code! When a new format is added or removed, it not only updates the new dictionary, but it changes the defaults themselves! That's not good. We want to create a new dictionary with the updates, not change the original.

Fix the bug by making add_format and remove_format pure functions that don't mutate their inputs.
"""

"""
def add_format(default_formats, new_format):
    default_formats[new_format] = True
    return default_formats


def remove_format(default_formats, old_format):
    default_formats[new_format] = False
    return default_formats
"""

# My solution
def add_format(default_formats, new_format):
    new_formats = default_formats.copy()
    new_formats[new_format] = True
    return new_formats


def remove_format(default_formats, old_format):
    new_formats = default_formats.copy()
    new_formats[old_format] = False
    return new_formats
