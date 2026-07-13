"""
Assignment
Our influencers need to travel to conferences to shill their sponsor's products! 
Since none of them trust Google Maps, they want to put in their proposed route to LockedIn, and we will tell them if their route is short enough to be worth their time (can you say feature creep?).

Complete the tsp function by performing a brute-force search using the provided algorithm. 
The brute-force search will, unfortunately, take factorial time, O(n!), because you will need to try all possible paths and keep track of the shortest.

The provided permutations() will give you all the possible permutations of a list. 

For example, permutations([0,1,2]) returns:

[
  [0, 1, 2],
  [0, 2, 1],
  [1, 0, 2],
  [1, 2, 0],
  [2, 0, 1],
  [2, 1, 0]
]
"""

"""
Pseudocode

Inputs:
- cities: A list of numbers starting from 0 that each represent a city.
- paths: A matrix where each point represents the distance between two cities.
- dist: The distance we are trying to beat.

Here's an example of the paths matrix (a list of lists). 
Each list represents the distance from that city to all the other cities. 
For example, paths[0][1] holds the distance from city 0 to city 1. paths[0][1] = paths[1][0]

paths = [
    [0, 12, 30], # list 0 shows the distance from city 0 to cities 0, 1 and 2
    [12, 0, 15], # list 1 shows the distance from city 1 to cities 0, 1 and 2
    [30, 15, 0], # list 2 shows the distance from city 2 to cities 0, 1 and 2
]

# all of the routes and their distances:

paths[0][1] # 12
paths[0][2] # 30
paths[1][2] # 15

# the shortest distance between all cities is from city 0 to city 1 to city 2, which is 12

Algorithm:
1. Use the permutations function to get the matrix of all possible paths through the given cities. Where the first path, [0, 1, 2] represents moving from city 0 -> city 1 -> city 2
2. Iterate over each possible path (permutation)
    1. Sum the distances between each city in the path using the paths matrix to look up the distances
    2. If the total distance of the path is less than the given dist return True
3. If no short paths were found, return False

You'll want to use a nested loop here! An outer loop over all permutations (paths), and an inner loop to sum the distances of consecutive city pairs within a single path

(!) Be careful with print statements. They will drastically slow down your code.
"""

def tsp(cities: list[int], paths: list[list[int]], dist: int) -> bool:
    perms = permutations(cities)

    for path in perms:
        distance = 0

        for i in range(len(path) - 1):
            distance += paths[path[i]][path[i + 1]]

        if distance < dist:
            return True
    return False


# don't touch below this line


def permutations(arr: list[int]) -> list[list[int]]:
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res: list[list[int]], arr: list[int], n: int) -> list[list[int]]:
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res
