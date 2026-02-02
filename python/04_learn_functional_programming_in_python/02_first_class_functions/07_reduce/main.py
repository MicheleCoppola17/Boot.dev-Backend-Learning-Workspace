"""
Assignment:
Complete the join and the join_first_sentences functions.

1. Complete the join function. It's a helper function we'll use in join_first_sentences.
    1. It takes two inputs:
        1. A doc_so_far accumulator string - similar to the sum_so_far variable in the example above.
        2. A sentence string - this is the next string we want to add to the accumulator.
    2. Returns the result of concatenating the "doc" and "sentence" strings together, with a period and a space in between. For example:

doc = "This is the first sentence"
sentence = "This is the second sentence"
print(join(doc, sentence))
# This is the first sentence. This is the second sentence

2. Complete the join_first_sentences function.
    1. It accepts two arguments:
        1. A list of sentence strings
        2. An integer n
    2. Only use the first n sentences from the list. If n is zero, just return an empty string.
    3. Use functools.reduce() with your join function to combine the sliced sentences into a single string.
    4. Add a final period without a trailing space and return this string.

Use list slicing to get the first n sentences.

Here's an example of the expected behavior:

joined = join_first_sentences(
    ["This is the first sentence", "This is the second sentence", "This is the third sentence"],
    2
)
print(joined)
# This is the first sentence. This is the second sentence.
"""

import functools


def join(doc_so_far, sentence):
    return doc_so_far + ". " + sentence


def join_first_sentences(sentences, n):
    if n == 0:
        return ""
    return functools.reduce(join, sentences[:n]) + "."
