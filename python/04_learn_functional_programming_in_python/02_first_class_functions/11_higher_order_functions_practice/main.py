"""
Assignment:
Complete the restore_documents function in one line - if you can. It takes two tuples of document strings, originals and backups, as input and returns a set.

1. Convert all documents to the same case with .upper() for comparison.
2. Filter out documents that are corrupted strings of random numbers with .isdigit().
3. Return a set that combines (and deduplicates) the documents from originals and backups.
"""

# My implementation
def restore_documents(originals, backups):
    return set(
        map(str.upper, 
            filter(lambda x: not x.isdigit(), originals + backups))
    )

"""
# Boot.dev's implementation
def restore_documents(originals, backups):
    return set(
        filter(
            lambda doc: not doc.isdigit(),
            map(lambda doc: doc.upper(), originals + backups),
        )
    )
"""