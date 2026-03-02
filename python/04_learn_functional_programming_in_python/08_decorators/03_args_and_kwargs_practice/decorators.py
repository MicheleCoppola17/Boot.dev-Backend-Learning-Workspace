"""
Assignment
Complete the configure_plugin_decorator function. It decorates a func that takes keyword arguments **kwargs, but the wrapper function it returns takes positional arguments *args. The arguments passed to the wrapper will be a series of tuples, each a key/value pair.

1. Create a wrapper function that takes positional arguments *args:
    1. Within the wrapper function, convert the args into a dictionary with the dict function.
    2. Return the result of calling func and passing this dictionary as keyword arguments by unpacking it with the ** operator to unpack the dict.
2. Return the wrapper function.

plugin_config = configure_backups(("path", "~/duplicates"), ("prefix", "duplicate_"), ("extension", ".rtf"))

# plugin_config:
# {
#   "path": "~/duplicates",
#   "prefix": "duplicate_",
#   "extension": ".rtf",
# }
"""

def configure_plugin_decorator(func):
    def wrapper(*args):
        dict_args = dict(args)
        return func(**dict_args)
    return wrapper
