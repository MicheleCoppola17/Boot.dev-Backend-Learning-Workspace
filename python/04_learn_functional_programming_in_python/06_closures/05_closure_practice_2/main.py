"""
Assignment
CSS uses selectors to identify the HTML element to add the style property. Essentially, styles are a chain of keys and values.

p {
  color: red;
}

- Selector: p (targets all <p> elements)
- Property: color
- Value: red

Complete the css_styles function. It accepts a nested dictionary as input, initial_styles, and returns a function, add_style.

1. Copies initial_styles to avoid modifying the original dictionary.

(!) Because we're dealing with nested dictionaries here, the .copy() method will produce a shallow copy: the outer dict is a new object, but mutating inner dicts will still affect the original one. So, you should import copy and use copy.deepcopy() instead.

2. Returns an add_style function that:
    1. Takes three string arguments: selector, property, and value. selector is a key in the initial_styles dictionary and its value should be a dictionary.
    2. Checks if the selector exists in the dictionary. If not, creates a new dictionary for the selector value.
    3. Then adds or updates the property with the given value for the selector dictionary.
    4. Returns the updated dictionary.

For example:

initial_styles = {
    "body": {
        "background-color": "white",
        "color": "black"
    },
    "h1": {
        "font-size": "16px",
        "padding": "10px"
    }
}

add_style = css_styles(initial_styles)

new_styles = add_style("p", "color", "grey")
# {
#    "body": {
#        "background-color": "white",
#        "color": "black"
#    },
#    "h1": {
#        "font-size": "16px",
#        "padding": "10px"
#    },
#    "p": {
#        "color": "grey",
#    }
# }
"""
import copy

def css_styles(initial_styles):
    initial_styles_copy = copy.deepcopy(initial_styles)
    def add_styles(selector, property, value):
        if selector not in initial_styles_copy:
            initial_styles_copy[selector] = {}
        initial_styles_copy[selector][property] = value
        return initial_styles_copy
    return add_styles
