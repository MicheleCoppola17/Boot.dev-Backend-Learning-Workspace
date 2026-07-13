"""
Assignment
Complete the verify_tsp function by implementing the algorithm below. Notice that it runs in polynomial time.

Pseudocode
Inputs:
- paths: A matrix where each point represents the distance between the two cities. For example, paths[cityA][cityB] holds the distance from cityA to cityB. paths[cityA][cityB] = paths[cityB][cityA]
- dist: The distance we are trying to find a path shorter than
- actual_path: The path we are trying to verify

Algorithm:
1. Loop over each city in the actual path
2. Sum the distance between each city in the actual path
3. If the sum is less than dist, return True, otherwise return False
"""

def verify_tsp(paths: list[list[int]], dist: int, actual_path: list[int]) -> bool:
    distance = 0
    for i in range(len(actual_path) - 1):
        distance += paths[actual_path[i]][actual_path[i + 1]]

    if distance < dist:
        return True
    return False
