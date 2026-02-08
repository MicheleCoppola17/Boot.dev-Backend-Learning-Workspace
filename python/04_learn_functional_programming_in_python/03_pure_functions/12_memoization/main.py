"""
Assignment
Counting the words in a document can be slow, so we want to memoize it.

Complete the word_count_memo function. It takes two inputs:

1. A document string.
2. A memos dictionary. The keys are full document strings, and the values are the word count of the document.

It should return two values:

1. The word count of the given document
2. An updated memos dictionary.

Here are the steps to follow:

1. Create a .copy() of the memos dictionary.
2. If the document is in the memos dictionary, just return the associated word count and the memos copy. No need to recompute the word count.
3. Otherwise, use the provided word_count function to count the words in the given document.
4. Store the word count in the memos copy.
5. return the word count and the updated memos copy.
"""

def word_count_memo(document, memos):
    memos_copy = memos.copy()
    if document in memos_copy:
        return memos_copy[document], memos_copy
    memos_copy[document] = word_count(document)
    return word_count(document), memos_copy

# Don't edit below this line


def word_count(document):
    count = len(document.split())
    return count
