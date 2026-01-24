"""
Assignment:
We need to filter the profanity out of our game's live chat feature! Complete the filter_messages function. 
It takes a list of chat messages as input and returns 2 new lists:

1. A list of the same messages but with all instances of the word dang removed.
2. A list containing the number of dang words that were removed from each message at that particular index.
Here are some examples:

messages = ["dang it bobby!", "look at it go"]
filter_messages(messages) # returns ["it bobby!", "look at it go"], [1, 0]

messages2 = ["That's the bloody dang Reaper of Mars...", "Pax au Telemanus!", "I was never taught how to use a dang razor!"]
filter_messages(messages2) # returns ["That's the bloody Reaper of Mars...", "Pax au Telemanus!", "I was never taught how to use a razor!"], [1, 0, 1]

Here are the steps for you to follow:

1. Create the 2 empty lists that you'll return at the end:
    1. One for the filtered messages with "dang" removed.
    2. And one for the counts of dangs removed from those messages.
2. For each message in the list of messages:
    1. Split the message into a list of words using the .split() string method.
    2. Create an empty list for all the good words in this message.
    3. Create another empty list for all the dangs in this message.
    4. For each word in the message:
        1. If the word is "dang", add it to the list of dangs
        2. If it is not "dang", add it to the list of good words
    5. Join the list of good words into a single string using the .join() method.
    6. Append the new filtered message to the list of filtered messages.
    7. Append the length of the list of dangs to the list of counts of dangs.
3. Return the filtered messages first, then the counts of dangs
"""

def filter_messages(messages):
    filtered_messages = []
    dang_counts = []

    for message in messages:
        words = message.split()
        good_words = []
        dangs = []
        for word in words:
            if word == "dang":
                dangs.append(word)
            else:
                good_words.append(word)
        filtered_message = " ".join(good_words)
        filtered_messages.append(filtered_message)
        dang_counts.append(len(dangs))

    return filtered_messages, dang_counts
        
