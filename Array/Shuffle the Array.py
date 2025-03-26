# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

 
# Example 1:
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7] 
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].


# Example 2:
# Input: nums = [1,2,3,4,4,3,2,1], n = 4
# Output: [1,4,2,3,3,2,4,1]


# Example 3:
# Input: nums = [1,1,2,2], n = 2
# Output: [1,2,1,2]


from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # IMPORTANT NOTE: https://leetcode.com/problems/shuffle-the-array/discuss/675956/In-Place-O(n)-Time-O(1)-Space-With-Explanation-and-Analysis
        i = 0
        for j in range(n, len(nums)):
            nums[j] = nums[j] << 10
            nums[j] = nums[j] | nums[i]
            i += 1
        
        i = 0
        for j in range(n, len(nums)):
            x = nums[j] & 1023
            y = nums[j] >> 10
            
            nums[i] = x
            nums[i + 1] = y
            i += 2
        return nums
# Time complexity: O(n)
# Space complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.shuffle([2,5,1,3,4,7], 3))
    print(sol.shuffle([1,2,3,4,4,3,2,1], 4))
    print(sol.shuffle([1,1,2,2], 2))