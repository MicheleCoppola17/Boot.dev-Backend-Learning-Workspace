"""
Assignment:
Fix the format_line function. It should apply the following transformations in order:

1. Strip whitespace from the beginning and end of the line.
2. Capitalize every character in the line.
3. Remove any periods from the line.
4. Append an ellipsis ... to the end of the line: words go here...

Run the code. You should see that some subtle bugs are present.

Break up the function to make it easier to debug. Use print() statements to see what's going on at each step.
"""
"""
# Initial function:
def format_line(line):
    return f"{line.rstrip().capitalize().replace(',', '')}...."
"""

def format_line(line):
    stripped = line.strip()
    capitalized = stripped.upper()
    no_point = capitalized.replace(".", "")
    suffixed = no_point + "..."
    return suffixed
