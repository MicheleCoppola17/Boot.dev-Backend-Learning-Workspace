"""
Assignment:
With the popularity of generative AI (like ChatGPT), we need to be able to convert files into pure text to be injected into prompts.

Complete the file_to_prompt function. It should take a file dictionary and a to_string function as inputs and return a formatted string.

1. Call the provided to_string function with file as an argument. The function is responsible for converting the file dictionary into a string: you don't need to implement it.
2. Wrap the result of the to_string function in triple backticks (```) to format it as a code block in Markdown. For example:

an example string

should become:

```
an example string
```
"""

def file_to_prompt(file, to_string):
    stringified = to_string(file)
    return f"```\n{stringified}\n```"
