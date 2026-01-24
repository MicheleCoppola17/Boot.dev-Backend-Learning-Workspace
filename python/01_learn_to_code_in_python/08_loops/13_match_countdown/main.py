"""
Assignment:
Complete the countdown_to_start function.

1. Write a loop that counts down from 10 to 1. At each iteration, print the number with an ellipsis:
- 10...
- 9...
- 8...
- etc.
2. However, when i is 1, print "Fight!" additionally:
- 1...Fight!

Do not use the ellipsis (…) character. Use three periods (...) instead.
"""

def countdown_to_start():
    for i in range(10, 0, -1):
        if i == 1:
            print(f"{i}...Fight!")
        else:
            print(f"{i}...")


# Don't edit below this line


def test():
    print("Counting down to match start:")
    countdown_to_start()
    print("=====================================")


def main():
    test()


main()
