# Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

# A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

# Return the maximum length of a subarray with positive product.

 
# Example 1:
# Input: nums = [1,-2,-3,4]
# Output: 4
# Explanation: The array nums already has a positive product of 24.

# Example 2:
# Input: nums = [0,1,-2,-3,-4]
# Output: 3
# Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
# Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.

# Example 3:
# Input: nums = [-1,-2,-3,0,1]
# Output: 2
# Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].


from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = 0
        i = 0
        while i < len(nums):
            countPositives = countNegatives = 0

            start = i
            # skip all the zeros
            while i < len(nums) and nums[start] == 0:
                start += 1
            
            end = start
            firstNegativePos = -1
            lastNegativePos = -1

            # finding  endpoint of the possible subarray
            while end < len(nums) and nums[end] != 0:
                if nums[end] > 0:
                    countPositives += 1
                else:
                    countNegatives += 1
                    if firstNegativePos == -1:
                        firstNegativePos = end
                    lastNegativePos = end
                end += 1
            
            # if number of negatives is even, then the whole subarray is positive
            if countNegatives & 1  == 0:
                ans = max(ans, end - start)
            else:
                # [X, -1, X, -2, X, -3, X]
                # ----------------         (firstHalf : even number of negatives)
                #         ---------------- (secondHalf : even number of negatives)
                firstHalf = lastNegativePos - start + 1
                secondHalf = end - firstNegativePos
                ans = max(ans, firstHalf, secondHalf)

            # why i = end + 1?
            # because nums[end] is now 0
            # so maybe end + 1 is non-zero
            i = end + 1
        return ans
# Time Complexity: O(n)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.getMaxLen([1,-2,-3,4]))
    print(sol.getMaxLen([0,1,-2,-3,-4]))
    print(sol.getMaxLen([-1,-2,-3,0,1]))