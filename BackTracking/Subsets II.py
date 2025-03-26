# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]


# Example 2:
# Input: nums = [0]
# Output: [[],[0]]


from typing import List


class Solution:
    def helper(self, nums, i, subset):
        self.ans.append(subset[:])

        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j - 1]:
                continue
            subset.append(nums[j])
            self.helper(nums, j + 1, subset)
            subset.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ans = []
        self.helper(nums, 0, [])
        return self.ans
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)


if __name__ == '__main__':
    sol = Solution()
    print(sol.subsetsWithDup([1,2,2]))
    print(sol.subsetsWithDup([0]))