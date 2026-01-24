"""
Assignment:
Dragons are egotistical creatures, let's give them a great format for announcing their presence in "Age of Dragons". 
When print() is called on an instance of a Dragon, the string "I am NAME, the COLOR dragon" should be printed.

Where NAME is the name of the dragon, and COLOR is its color.
"""

class Dragon:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"I am {self.name}, the {self.color} dragon"
