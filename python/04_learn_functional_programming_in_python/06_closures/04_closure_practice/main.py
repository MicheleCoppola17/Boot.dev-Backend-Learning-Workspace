"""
Assignment
Doc2Doc needs a function to manage a growing collection of documents.

Complete the new_collection function. It accepts:

- initial_docs: a list of strings

The new_collection function should:

1. Create a copy of initial_docs (don't modify the original list!)
2. Return a new function, add_doc, that:
    1. Accepts a single string argument (a document to add)
    2. Appends that document to the copied list from step 1
    3. Returns the updated list

Each time you call the returned function, it should add to the same list (the closure keeps track of the list's state).

Example Usage:
my_collection = new_collection(["doc1", "doc2", "doc3"])
print(my_collection("doc4"))
# ['doc1', 'doc2', 'doc3', 'doc4']
print(my_collection("doc5"))
# ['doc1', 'doc2', 'doc3', 'doc4', 'doc5']
"""

def new_collection(initial_docs):
    initial_docs_copy = initial_docs.copy()
    def add_doc(doc):
        initial_docs_copy.append(doc)
        return initial_docs_copy
    return add_doc  
