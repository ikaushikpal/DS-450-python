# Given the mobile numeric keypad. You can only press buttons that are up, left, right, or down to the current button. You are not allowed to press bottom row corner buttons (i.e. * and # ). Given a number N, the task is to find out the number of possible numbers of the given length.


# Example 1:
# Input: 1
# Output: 10
# Explanation: Number of possible numbers 
# would be 10 (0, 1, 2, 3, …., 9)  


# Example 2:
# Input: N = 2
# Output: 36
# Explanation: Possible numbers: 00, 08, 11,
# 12, 14, 22, 21, 23, 25 and so on.
# If we start with 0, valid numbers 
# will be 00, 08 (count: 2)
# If we start with 1, valid numbers 
# will be 11, 12, 14 (count: 3)
# If we start with 2, valid numbers 
# will be 22, 21, 23,25 (count: 4)
# If we start with 3, valid numbers 
# will be 33, 32, 36 (count: 3)
# If we start with 4, valid numbers 
# will be 44,41,45,47 (count: 4)
# If we start with 5, valid numbers 
# will be 55,54,52,56,58 (count: 5) 
# and so on..


class Solution:
    def getCount(self, n):
        dp = [1] * 10
        moves = {0:[8], 
                1:[2, 4], 
                2:[1, 3, 5], 
                3:[2, 6],
                4:[1, 5, 7],
                5:[2, 6, 8, 4],
                6:[3, 5, 9],
                7:[4, 8], 
                8:[5, 9, 0, 7],
                9:[6, 8]}

        for _ in range(2, n+1):
            newDp = [0] * 10
            for i in range(0, 10):
                newDp[i] = dp[i]
                for j in moves[i]:
                    newDp[i] += dp[j]
            dp = newDp
        
        return sum(dp)
# Time Complexity: O(N*10*4) = O(N)
# Space Complexity: O(10 + 10) = O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.getCount(1))
    print(sol.getCount(2))