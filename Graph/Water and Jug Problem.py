# You are given two jugs with capacities jug1Capacity and jug2Capacity liters. There is an infinite amount of water supply available. Determine whether it is possible to measure exactly targetCapacity liters using these two jugs.

# If targetCapacity liters of water are measurable, you must have targetCapacity liters of water contained within one or both buckets by the end.

# Operations allowed:

# Fill any of the jugs with water.
# Empty any of the jugs.
# Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.
 

# Example 1:
# Input: jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
# Output: true
# Explanation: The famous Die Hard example 

# Example 2:
# Input: jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
# Output: false

# Example 3:
# Input: jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
# Output: true


# CHECK : https://www.youtube.com/watch?v=0Unzj1hcsIw

from collections import deque


class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        
        moves = [jug1Capacity, -jug1Capacity, jug2Capacity, -jug2Capacity]
        queue = deque()
        queue.append(0)
        visited = set([0])

        while queue:
            curr = queue.popleft()
            if curr == targetCapacity:
                return True

            for move in moves:
                nextJug = curr + move
                if nextJug == targetCapacity:
                    return True

                if 0<=nextJug < jug1Capacity + jug2Capacity and nextJug not in visited:
                    queue.append(nextJug)
                    visited.add(nextJug)    
        
        return False
# Time Complexity: O(N)
# Space Complexity: O(N)


class Solution:
    def gcd(self, x, y):
        while y:
            x, y = y, x % y
        return x

    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        # https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity#:~:text=In%20mathematics%2C%20B%C3%A9zout's%20identity%20(also,that%20ax%20%2B%20by%20%3D%20d.
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        
        return targetCapacity % self.gcd(jug1Capacity, jug2Capacity) == 0
# Time Complexity: O(log(min(jug1Capacity, jug2Capacity)))
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.canMeasureWater(3, 5, 4))
    print(sol.canMeasureWater(2, 6, 5))
    print(sol.canMeasureWater(1, 2, 3))
