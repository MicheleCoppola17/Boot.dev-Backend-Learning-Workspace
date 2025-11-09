"""
ASSIGNMENT:
Due to the constraints of our app's server, there is a maximum number of players we can have on a single Fantasy Quest server.

Complete the max_players_on_server function. It takes no inputs, but simply returns 3 static numbers:

1. The max players on a "small" server: 1,024,000,000,000,000,000 (1.024e18)
2. The max players on a "medium" server: 10,240,000,000,000,000,000
3. The max players on a "large" server: 102,400,000,000,000,000,000
Use scientific notation to represent these numbers. For example: 3.104e15.

(Numbers in scientific notation are floats. For example, 1.024e18 is actually equivalent to 1,024,000,000,000,000,000.0 (note the .0 at the end).
This is expected and perfectly fine for this assignment.)
"""

def max_players_on_server():
    return 1.024e18, 1.024e19, 1.024e20