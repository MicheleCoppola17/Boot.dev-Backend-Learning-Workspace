"""
Assignment:
Complete the pair_document_with_format function. It takes two lists of strings as input:

- doc_names: the names of documents
- doc_formats: the file formats of the documents

1. zip up the lists into a single list of tuples with the names as the first index and the formats as the second index in each tuple.
2. filter the list of tuples to only include tuples where the format is one of the given valid_formats.

Return the result as a list.
"""

valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

# Don't edit above this line

# My implementation
def pair_document_with_format(doc_names, doc_formats):
     return list(filter(lambda doc: doc[1] in valid_formats, zip(doc_names, doc_formats)))

"""
# Boot.dev's solution
def pair_document_with_format(doc_names, doc_formats):
    zipped = list(zip(doc_names, doc_formats))
    return list(filter(lambda x: x[1] in valid_formats, zipped))
"""
