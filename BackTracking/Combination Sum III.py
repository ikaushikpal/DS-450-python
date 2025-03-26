# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.


# Example 1:
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Explanation:
# 1 + 2 + 4 = 7
# There are no other valid combinations.


# Example 2:
# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations.


# Example 3:
# Input: k = 4, n = 1
# Output: []
# Explanation: There are no valid combinations.
# Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.


from typing import List


class Solution:
    def helper(self, i, combi, k, n):
        if k == 0 and n == 0:
            self.ans.append(combi[:])
            return
        
        if n < 0 or k == 0:
            return
        
        for j in range(i, 10):
            combi.append(j)
            self.helper(j+1, combi, k-1, n-j)
            combi.pop()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        self.helper(1, [], k, n)
        return self.ans
# Time Complexity: O(9^k)
# because each recursive call iterates through at most all options (integers [1, 9] in this problem), and we do so for each of the k positions in the combination we are currently trying to build.
# Space Complexity: O(k)


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum3(3, 7))
    print(sol.combinationSum3(3, 9))
    print(sol.combinationSum3(4, 1))