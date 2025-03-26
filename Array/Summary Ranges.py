# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b
 

# Example 1:
# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"


# Example 2:
# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"


from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        N = len(nums)
        i, ans = 0, []
        
        while i < N:
            j = 0
            start = nums[i]
            
            while i + j < N and start + j == nums[i + j] :
                j += 1
            
            end = nums[i + j - 1]
            if start == end:
                ans.append(f'{start}')
            else:
                ans.append(f'{start}->{end}')
            i += j
        return ans
# Time Complexity: O(N)
# Space Complexity: O(N)


if __name__ == "__main__":
    sol = Solution()
    print(sol.summaryRanges([0,1,2,4,5,7]))
    print(sol.summaryRanges([0,2,3,4,6,8,9]))

    