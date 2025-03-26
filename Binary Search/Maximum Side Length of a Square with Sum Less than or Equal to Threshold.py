# Given a m x n matrix mat and an integer threshold, return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.


# Example 1:
# Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
# Output: 2
# Explanation: The maximum side length of square with sum less than 4 is 2 as shown.


# Example 2:
# Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
# Output: 0


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        if not mat:
            return 0
        max_square = 0
        dp = [[0] * (len(mat[0]) + 1) for _ in range(len(mat) + 1)]
        for i in range(1, len(mat) + 1):
            for j in range(1, len(mat[0]) + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i - 1][j - 1]
                l = 1
                r = min(i, j)
                while l <= r:
                    k = (l + r) // 2
                    cur_sum = dp[i][j] - dp[i - k][j] - dp[i][j - k] + dp[i - k][j - k]
                    if cur_sum <= threshold:
                        max_square = max(max_square, k)
                        l = k + 1
                    else:
                        r = k - 1
        return max_square