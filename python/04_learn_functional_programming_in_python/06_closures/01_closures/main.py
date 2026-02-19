"""
Assignment
Doc2Doc keeps track of how many words are in a collection of documents.

1. Complete the word_count_aggregator function.
    1. It should return a function that calculates the number of words in its input string, doc.
    2. It should then add that number to an enclosed count value and return the new count.
In other words, it keeps a running total of the count variable within a closure.
"""

def word_count_aggregator():
    count = 0
    def word_counter(doc):
        nonlocal count
        count += len(doc.split())
        return count
    return word_counter