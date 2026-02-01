"""
Assignment:
Debug the hex_to_rgb function. hex_to_rgb should take a hex triplet color code and return three integers for the RGB values using int().

1. Some of the arguments passed to int() on lines 4, 5, and 6 are incorrect. Review the linked documentation to see how to convert hexadecimal (base 16) values.
2. Use the provided is_hexadecimal function inside of hex_to_rgb to check if hex_color is valid. If the input is not a six character long hexadecimal string, raise the exception "not a hex color string".

Example:

red_val, green_val, blue_val = hex_to_rgb("A020F0")

print(red_val)
# prints 160

print(green_val)
# prints 32

print(blue_val)
# prints 240
"""

def hex_to_rgb(hex_color):
    if not is_hexadecimal(hex_color) or len(hex_color) != 6:
        raise Exception("not a hex color string")
    r = int(hex_color[:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:], 16)
    return r, g, b


# Don't edit below this line


def is_hexadecimal(hex_string):
    try:
        int(hex_string, 16)
        return True
    except Exception:
        return False
