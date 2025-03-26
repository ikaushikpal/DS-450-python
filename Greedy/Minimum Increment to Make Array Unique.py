# You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.
# Return the minimum number of moves to make every value in nums unique.
# The test cases are generated so that the answer fits in a 32-bit integer.


# Example 1:
# Input: nums = [1,2,2]
# Output: 1
# Explanation: After 1 move, the array could be [1, 2, 3].


# Example 2:
# Input: nums = [3,2,1,2,1,7]
# Output: 6
# Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
# It can be shown with 5 or less moves that it is impossible for the array to have all unique values.


import collections
from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        i, ans = nums[0], 0
        for num in nums:
            if num < i:
                ans += i - num
            i = max(i, num) + 1
        return ans
# T.C. = O(NlogN)
# S.C. = O(N)


class Solution:
    def minIncrementForUnique(self, A):
        c = collections.Counter(A)
        res = need = 0
        for x in sorted(c):
            res += c[x] * max(need - x, 0) + c[x] * (c[x] - 1) / 2
            need = max(need, x) + c[x]
        return res
# T.C. = O(Klogk) where K is the unique numbers
# S.C. = O(N)

if __name__ == '__main__':
    sol = Solution()
    print(sol.minIncrementForUnique(nums = [1,2,2]))
    print(sol.minIncrementForUnique(nums = [3,2,1,2,1,7]))