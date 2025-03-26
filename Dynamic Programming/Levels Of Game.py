# You are playing a game. At each level of the game, you have to choose one of the roads to go to the next level. Initially, you have h amount of health and m amount of money.
# If you take the first road then health decreases by 20 and money increase by 5. If you take the second road then your health decreases by 5 and money decrease by 10. If you take the third road then your health increases by 3 and money increase by 2.
# You have to tell what is the maximum level you can reach up to under the constraints that in no two consecutive levels you can select the same road twice and once your health or money becomes <= 0 game ends(that level is not counted).


# Example 1:
# Input:
# H=2
# M=10
# Output:
# 1
# Explanation:
# For the first level, we can only choose the third road.
# Now we cannot move ahead anymore.


# Example 2:
# Input:
# H=20
# M=8
# Output:
# 5
# Explanation:
# Go like this:- R3(23,10)->R1(3,15)->R3(6,17)->
# R2(1,7)->R3(4,9)-> game ends as we cannot choose
# any more roads.


from typing import List


class Solution:
    def helper(self, h, m, prev):
        if h <= 0 or m <= 0:
            return 0
        
        if (h, m, prev) in self.memo:
            return self.memo[(h, m, prev)]
            
        maxLevel = 0
        if prev != 0:
            maxLevel = max(maxLevel, self.helper(h-20, m+5, 0))
        
        if prev != 1:
            maxLevel = max(maxLevel, self.helper(h-5, m-10, 1))
            
        if prev != 2:
            maxLevel = max(maxLevel, self.helper(h+3, m+2, 2))
            
        self.memo[(h, m, prev)] = 1 + maxLevel
        return 1 + maxLevel
        
    def maxLevel(self, h:int,m:int) -> int:
        self.memo = {}
        return self.helper(h, m, -1) - 1
# Time Complexity: O(H*M*3) = O(H*M)
# Space Complexity: O(H*M*3) = O(H*M)


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxLevel(2, 10))
    print(sol.maxLevel(20, 8))