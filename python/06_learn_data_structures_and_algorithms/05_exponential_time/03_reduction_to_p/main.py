"""
Assignment
Our data scientists at LockedIn have found that the growth of the average influencer's follow count is roughly the same growth rate as the Fibonacci sequence! In other words, after 6 weeks of good social media posts, the average influencer will have 8 followers. After 7 weeks, 13 followers, and so on.

The trouble is, our current implementation of the fib function takes so long (exponential time!) to complete that when our influencers navigate to their analytics page it often never completes loading!

Adjust the fib function using the given algorithm to achieve polynomial runtime.

Here are the implementation details to do it in polynomial time:

1. The input n represents the index of the desired Fibonacci number.
2. If n is less than or equal to 1, then return n.
3. Initialize three variables: grandparent = 0, parent = 1, and a placeholder current to store the new Fibonacci number at each step.
4. Write a loop that iterates n - 1 times. (For example, if n = 2, one iteration occurs.)
5. Inside the loop:
    1. Set current = parent + grandparent
    2. Adjust the ancestor values (parent and grandparent) to maintain the sequence.
6. Once the loop completes, return current.
"""

# Exponential Implementation
"""
def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
"""

def fib(n: int) -> int:
    if n <= 1:
        return n
    grandparent, parent = 0, 1
    current = 0
    for i in range (n-1):
        current = parent + grandparent
        grandparent = parent
        parent = current

    return current


