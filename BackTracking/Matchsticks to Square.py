# You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

# Return true if you can make this square and false otherwise.

# Example 1:

# Input: matchsticks = [1,1,2,2,2]
# Output: true
# Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

# Example 2:

# Input: matchsticks = [3,3,3,3,4]
# Output: false
# Explanation: You cannot find a way to form a square with all the matchsticks.


from typing import List


class Solution:
    def dfs(self, sticks, matchsticks, index, length):
        # found one solution
        if index == len(matchsticks):
            return True
        
        for i in range(4):
            ith_side_length = sticks[i] + matchsticks[index]
            
            # if ith_side_length is less than  or equal the square's length, then
            # there is a chance it may be a solution
            if ith_side_length <= length:
                sticks[i] = ith_side_length
                # if the solution is found, return true
                if self.dfs(sticks, matchsticks, index + 1, length):
                    return True
                # if it is not a solution, then restore the sticks back to previous state
                sticks[i] -= matchsticks[index]
            
            # importance of this step
            # is that at first all sides are 0, so if we can not form square
            # at any side, we can not form square from other side also
            if index == 0:
                return False
        
        return False

    def makesquare(self, matchsticks: List[int]) -> bool:
        # if sum of matchsticks is not divisible by 4, return false
        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        length = total // 4
        # sorting in reversing in order to make it fast
        matchsticks.sort(reverse=True)

        # one matchstick's length is higher than the square's length, then no way we can form square
        if matchsticks[0] > length:
            return False        
        
        sticks = [0] * 4
        return self.dfs(sticks, matchsticks, 0, length)
# it is a decision problem and we can solve it using backtracking
# Time Complexity: O(4^n) because for each stick it has choice to be part of any 4 sides
# space complexity: O(n) for stack space


if __name__ == '__main__':
    sol = Solution()
    print(sol.makesquare([1,1,2,2,2]))
    print(sol.makesquare([3,3,3,3,4]))
    print(sol.makesquare([1, 2, 6, 3, 4, 3, 2, 3]))