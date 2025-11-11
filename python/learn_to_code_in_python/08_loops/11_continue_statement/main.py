"""
Assignment:
In Fantasy Quest, we want to grant the player an enchantment each time they complete three quests. 
And the higher the number of total quests completed, the stronger the enchantment.

Fix the award_enchantments function. It calculates the strength of the enchantment - 5 times the total number of quests completed - and prints a message for the player. 
But we need to make sure this happens only once for every three quests within the loop!

1. At the beginning of the function, before the loop, initialize a counter variable to 0.
2. Within the for loop:
- Add 1 to counter in each iteration, to keep track of how many quests we've seen.
- If counter is less than 3, continue to the next iteration.
- Otherwise, we must have completed 3 quests! Reset counter to 0 before the enchantment is awarded.

Example:

award_enchantments(2, 8, 1)
# loop through the quests:
# 2 -> first quest: continue
# 3 -> second quest: continue
# 4 -> third quest: "Enchantment of strength 20 awarded for completing 4 quests!"
# 5 -> first quest: continue
# 6 -> second quest: continue
# 7 -> third quest: "Enchantment of strength 35 awarded for completing 7 quests!"
"""

def award_enchantments(start, end, step):
    counter = 0
    for quest_number in range(start, end, step):
        counter += 1
        enchantment_strength = quest_number * 5
        if counter < 3:
            continue
        counter = 0
        print(
            f"Enchantment of strength {enchantment_strength} awarded for completing {quest_number} quests!"
        )


# Don't touch below this line


def test(start, end, step):
    print(f"Testing with quests {start} through {end - 1}:")
    award_enchantments(start, end, step)
    print("========================================")


def main():
    test(1, 11, 1)
    test(20, 24, 1)
    test(10, 12, 1)
    test(11, 19, 1)


main()
