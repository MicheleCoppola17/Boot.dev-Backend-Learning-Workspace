"""
Assignment:
Complete the Card class:

1. Define a constructor that takes rank and suit as parameters and sets rank, suit, rank_index, and suit_index instance variables.
    - You will need the indexes of the ranks, and suits to help you compare them against each other. Keep in mind that a rank and a suit are just strings within a list.
2. Overload the following comparison operators so that they reflect the ranking explained in the next section:
    - ==: __eq__
    - >: __gt__
    - <: __lt__

Ranking the Cards
A card is "greater than" another card if it has a higher rank. However, if the ranks are the same, the card with the higher suit is "greater than" the other card. 
This same logic applies to the "less than" operator. The "equal to" operator should check that the rank AND suit are equal.

The suits and ranks are defined in the global SUITS and RANKS variables. The lower the index, the lower the rank or suit.

The .index list method is very useful when trying to determine the index of an element in a list.
"""

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_index = RANKS.index(rank)
        self.suit_index = SUITS.index(suit)

    def __eq__(self, other):
        return (
            self.rank_index == other.rank_index and 
            self.suit_index == other.suit_index
            )

    def __lt__(self, other):
        if self.rank_index == other.rank_index:
            return self.suit_index < other.suit_index
        return self.rank_index < other.rank_index

    def __gt__(self, other):
        if self.rank_index == other.rank_index:
            return self.suit_index > other.suit_index
        return self.rank_index > other.rank_index

    # don't touch below this line

    def __str__(self):
        return f"{self.rank} of {self.suit}"
