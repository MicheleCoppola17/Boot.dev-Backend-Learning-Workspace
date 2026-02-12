"""
Assignment:
You're responsible for a module in Doc2Doc that can scan a file system (represented in our code as nested dictionaries) and create a list of the filenames.

Complete the recursive list_files function. It accepts two arguments:

- parent_directory: A dictionary of dictionaries representing the current directory. A child directory's value is a dictionary and a file's value is None.
- current_filepath: A string representing the current path (e.g. /dir1/dir2/filename.txt)

It should return a list of all filepaths in the parent_directory.

Steps:
1. Create an empty list to store the file paths.
2. Use a for-loop to iterate through the keys of the parent_directory dictionary:
    1. Use the key to create a new file path by concatenating a slash / and the key to the end of the current_filepath.
    2. If the value is None, the key is a filename. .append() the new file path to the list of file paths.
    3. Otherwise, the value is a child directory dictionary. Recursively call list_files with the child directory dictionary and the new file path.
    4. Use .extend() to add the results of the recursive call to the list of file paths.
3. Return the list of file paths.

Example parent_directory:

{
    "Documents": {
        "Proposal.docx": None,
        "Receipts": {
            "January": {
                "receipt1.txt": None,
                "receipt2.txt": None
            },
            "February": {
                "receipt3.txt": None
            }
        }
    },
}

Resulting list of file paths:

[
    "/Documents/Proposal.docx",
    "/Documents/Receipts/January/receipt1.txt",
    "/Documents/Receipts/January/receipt2.txt",
    "/Documents/Receipts/February/receipt3.txt"
]
"""

def list_files(parent_directory, current_filepath=""):
    file_paths = []
    for key in parent_directory:
        new_filepath = current_filepath + f"/{key}"
        if parent_directory[key] is None:
            file_paths.append(new_filepath)
        else:
            file_paths.extend(list_files(parent_directory[key], new_filepath))
    return file_paths
