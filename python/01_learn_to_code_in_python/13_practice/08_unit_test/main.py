"""
Assignment:
Let's flip the script: in main.py you'll find a read-only, almost correct function called avg_luck_boost. 
It's used in Fantasy Quest to calculate the average "luck" boost granted to a party of players when they defeat a boss, to determine the loot that they receive. 

It can be used like this:

luck_boosts = [5, 3, 10]
avg_boost = avg_luck_boost(luck_boosts)
print(avg_boost)  # 6.0

Run the tests. Notice that they all pass! But there's a problem... some odd behavior isn't covered by the existing test cases.

What happens if no party member has a luck boost? The function will try to divide by zero, i.e. the length of the input list, and crash the program.

luck_boosts = []
avg_boost = avg_luck_boost(luck_boosts) # ZeroDivisionError

What we want this function to do if the input list is empty is to return 0.0. Add a test case to the list in test_cases.py to check for this behavior.

- Add an object to the list of run_cases, with luck_boosts set to an empty list, and expected_avg set to 0.0.

Don't worry, this test is meant to fail! We'll be fixing the function in the next lesson.
"""

def avg_luck_boost(luck_boosts):
    total = 0
    for boost in luck_boosts:
        total += boost
    return total / len(luck_boosts)
