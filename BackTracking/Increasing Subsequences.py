# Given an integer array nums, return all the different possible increasing subsequences of the given array with at least two elements. You may return the answer in any order.

# The given array may contain duplicates, and two equal integers should also be considered a special case of increasing sequence.


# Example 1:
# Input: nums = [4,6,7,7]
# Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]


# Example 2:
# Input: nums = [4,4,3,2,1]
# Output: [[4,4]]


from typing import List


class Solution:
    def dfs(self, nums, i=0, seq=[]):
        if len(seq) > 1:
            self.ans.add(tuple(seq))
        
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j - 1]:
                continue

            if len(seq) == 0 or seq[-1] <= nums[j]:
                seq.append(nums[j])
                self.dfs(nums, j + 1, seq)
                seq.pop()

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.ans = set()
        self.dfs(nums)
        return self.ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.findSubsequences([4,6,7,7]))