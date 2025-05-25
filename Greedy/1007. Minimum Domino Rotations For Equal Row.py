# In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

# We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

# Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

# If it cannot be done, return -1.

 
# Example 1:
# Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
# Output: 2
# Explanation: 
# The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.


# Example 2:
# Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
# Output: -1
# Explanation: 
# In this case, it is not possible to rotate the dominoes to make one row of values equal.
 

# Constraints:
# 2 <= tops.length <= 2 * 10^4
# bottoms.length == tops.length
# 1 <= tops[i], bottoms[i] <= 6


from typing import List


class Solution:
    def rotateNCheck(self, tops, bottoms, K):
        N = len(tops)
        count = 0

        for i in range(N):
            if tops[i] == K:
                continue
            
            if bottoms[i] == K:
                count += 1
            else:
                return float('inf')
        return count

    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        N = len(tops)
        domino_freq = [0] * 7
        
        for i in range(N):
            domino_freq[tops[i]] += 1
            
            if tops[i] != bottoms[i]:
                domino_freq[bottoms[i]] += 1
        
        min_cost = float('inf')
        for i in range(1, 7):
            if domino_freq[i] < N:
                continue
            
            min_cost = min(min_cost, self.rotateNCheck(tops, bottoms, i))
            min_cost = min(min_cost, self.rotateNCheck(bottoms, tops, i))

        if min_cost == float('inf'):
            return -1
        return min_cost
# Time Complexity: O(N)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minDominoRotations(tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]))
    print(sol.minDominoRotations(tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]))