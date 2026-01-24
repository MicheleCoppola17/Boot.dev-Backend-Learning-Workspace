"""
Assignment:
Fix the for loop in the count_down function. It takes start and end inputs, but start is always greater than end. 
It's supposed to print numbers counting down, beginning at start (inclusive) and stopping just before end (exclusive), but there's a mistake in the range function call.
"""

def count_down(start, end):
    for i in range(start, end, -1):
        print(i)


# Don't edit below this line


def test(start, end):
    print(f"Using inputs start: {start} and end: {end}")
    print(f"Printing numbers from {start} to {end + 1}:")
    count_down(start, end)
    print("=====================================")


def main():
    test(10, 0)
    test(20, 10)
    test(15, 11)


main()
