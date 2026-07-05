"""
Assignment
Complete the matchmake function that simulates users joining and leaving the matchmaking queue. The function should take a queue instance and a user tuple containing a name and action (either "join" or "leave"):

user = ('Bob', 'join')
user = ('Alice', 'leave')

For each call to matchmake:

1. If the action is "leave", search the queue for the user and remove them if they are in the queue.
2. If the action is "join", push the user's name onto the queue.
3. Lastly, check if the queue has at least 4 users in it. If so, pop the first 2 users from the queue and return the following string:
"{user1} matched {user2}!"

Where user1 is the first user popped and user2 is the second user popped.

4. If there were less than 4 users in the queue, return the following string: "No match found"
"""

from queue import Queue


def matchmake(queue: Queue, user: tuple[str, str]) -> str:
    if user[1] == 'leave':
        queue.search_and_remove(user[0])
    if user[1] == 'join':
        queue.push(user[0])
    if queue.size() >= 4:
        user_1 = queue.pop()
        user_2 = queue.pop()
        return f"{user_1} matched {user_2}!"
    return "No match found"
