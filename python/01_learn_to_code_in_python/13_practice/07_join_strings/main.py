"""
Assignment:
Complete the join_strings() function. It takes a list of strings and returns a new single string. 
The new string is the concatenation of all the input strings from the list end-to-end, in order, with a comma between them. 
If the list is empty, return an empty string.

For example:

string_list = ["Annie", "Reiner", "Bertholdt"]
joined_string = join_strings(string_list)
print(joined_string)
# "Annie,Reiner,Bertholdt"

string_list = ["Eren", "Mikasa", "Armin"]
joined_string = join_strings(string_list)
print(joined_string)
# "Eren,Mikasa,Armin"

Do not use the built-in .join() method... we're trying to learn how this works manually.

You shouldn't have commas at the beginning or end of the final string.
Remember, you can use negative indexes.
"""

# It works, but has a limitation with duplicate items of the last one: [a, b, b] -> a,bb
"""
def join_strings(strings):
    joined_string = ""
    for string in strings:
        if string != strings[-1]:
            joined_string += string + ","
        else:
            joined_string += string
    return joined_string
"""

def join_strings(strings):
    joined_string = ""
    for i in range(len(strings)):
        if i != len(strings) - 1:
            joined_string += strings[i] + ","
        else:
            joined_string += strings[i]
    return joined_string