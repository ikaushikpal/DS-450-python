# A split of an integer array is good if:

# The array is split into three non-empty contiguous subarrays - named left, mid, right respectively from left to right.
# The sum of the elements in left is less than or equal to the sum of the elements in mid, and the sum of the elements in mid is less than or equal to the sum of the elements in right.
# Given nums, an array of non-negative integers, return the number of good ways to split nums. As the number may be too large, return it modulo 109 + 7.

 

# Example 1:

# Input: nums = [1,1,1]
# Output: 1
# Explanation: The only good way to split nums is [1] [1] [1].


# Example 2:

# Input: nums = [1,2,2,2,5,0]
# Output: 3
# Explanation: There are three good ways of splitting nums:
# [1] [2] [2,2,5,0]
# [1] [2,2] [2,5,0]
# [1,2] [2,2] [5,0]


# Example 3:

# Input: nums = [3,2,1]
# Output: 0
# Explanation: There is no good way to split nums.


from typing import List

##################### not completed
class Solution:
    def findCeil(self, arr, low, high, key):
        res = -1

        while low <= high:
            mid = (low+high)//2

            if arr[mid] == key:
                return mid
            elif arr[mid] < key:
                low = mid + 1       
            else:
                res = mid
                high = mid - 1

        return res
    
    def findFloor(self, arr, low, high, key):
        res = -1

        while low <= high:
            mid = (low+high)//2

            if arr[mid] == key:
                return mid 
            elif arr[mid] < key:
                res = mid
                low = mid + 1
            else:
                high = mid - 1

        return res
    
    def waysToSplit(self, nums: List[int]) -> int:
        ans = 0
        
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        total_sum = prefix_sum[-1]
        
        for i in range(len(nums)-2):
            sum_i = prefix_sum[i]
            
            if sum_i > (total_sum - sum_i) // 2:
                break
                
            j = self.findCeil(prefix_sum, i+1, len(nums)-2, sum_i*2)
            k = self.findFloor(prefix_sum, j, len(nums)-1, sum_i + (total_sum - sum_i)//2)
            
            if k == -1 or j == -1:
                continue
                
            ans = (ans + (k - j + 1) % 1_000_000_007) % 1_000_000_007
            
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.waysToSplit([1,1,1]))
    print(sol.waysToSplit([1,2,2,2,5,0]))
    print(sol.waysToSplit([3,2,1]))