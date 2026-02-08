"""
Assignment
In Doc2Doc, we frequently need to change the casing of some text. For example:

TitleCase
Every Day Once A Day Give Yourself A Present
LowerCase
every day once a day give yourself a present
UpperCase
EVERY DAY ONCE A DAY GIVE YOURSELF A PRESENT

There is an issue in the convert_case function, our test suite can't test its behavior because it's printing to the console (eww... a side-effect) instead of returning a value. Fix the function so that it returns the correct value instead of printing it.
"""

def convert_case(text, target_format):
    if not text or not target_format:
        raise ValueError(f"no text or target format provided")

    if target_format == "uppercase":
        return text.upper()
    if target_format == "lowercase":
        return text.lower()
    if target_format == "titlecase":
        return text.title()
    raise ValueError(f"unsupported format: {target_format}")
