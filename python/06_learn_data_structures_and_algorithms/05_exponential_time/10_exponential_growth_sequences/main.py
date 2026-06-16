"""
Assignment
Complete the exponential_growth function. Given the initial followers count n, growth factor factor, and number of days days, return a list containing the exponential growth of followers for each day.

For example:

- Initial followers: 10
- Growth factor: 2
- Days: 4

Growth sequence: [10, 20, 40, 80, 160]
"""

def exponential_growth(n: int, factor: int, days: int) -> list[int]:
    growth_sequence = []
    days_counter = 0
    while days_counter <= days:
        growth_sequence.append(n)
        n *= factor
        days_counter += 1
    return growth_sequence
