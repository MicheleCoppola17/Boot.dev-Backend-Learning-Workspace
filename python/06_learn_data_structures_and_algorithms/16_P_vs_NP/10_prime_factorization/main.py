"""
The Algorithm
Given a large number, return a list of all the prime factors.

- prime_factors(8) -> [2, 2, 2]
- prime_factors(10) -> [2, 5]
- prime_factors(24) -> [2, 2, 2, 3]

1. Divide n by 2 as many times as you can evenly (no remainder). For each division, append a 2 to the list of prime factors.
2. By now, n must be odd. Start a loop that iterates over all odd numbers from 3 to the square root of n inclusive. Use math.sqrt(). For each number i:
    1. If n can be divided evenly by i, then divide n by i and append i to the list.
    2. Repeat this (nested loop) until n cannot be divided evenly by i, then move on to the next i.
3. If n is still greater than 2 after that loop, it must still be prime, so just append it to the list.
4. Return the list of primes, ordered from least to greatest.

Assignment
Complete the prime_factors function according to the given algorithm. Notice how the algorithm gets much slower as the size of the input (in bits) grows.

(!) The returned list should only contain ints, no floats.
"""

import math


def prime_factors(n: int) -> list[int]:
    pr_factors = []
    
    while n % 2 == 0:
        n /= 2
        pr_factors.append(2)
    
    for i in range(3, int(math.sqrt(n) + 1), 2):
        while n % i == 0:
            n /= i
            pr_factors.append(i)
    
    if n > 2:
        pr_factors.append(int(n))
    
    return sorted(pr_factors)        