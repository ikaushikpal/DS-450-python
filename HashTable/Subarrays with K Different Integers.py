# Given an integer array nums and an integer k, return the number of good subarrays of nums.

# A good array is an array where the number of different integers in that array is exactly k.

# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.

 

# Example 1:
# Input: nums = [1,2,1,2,3], k = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]


# Example 2:
# Input: nums = [1,2,1,3,4], k = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].


from typing import List


class Solution:
    def atmost(self, nums, k):
        freqMap = {}
        ans = i = 0
        
        for j, num in enumerate(nums):
            freqMap[num] = freqMap.get(num, 0) + 1

            while len(freqMap) > k:
                freqMap[nums[i]] -= 1
                
                if freqMap[nums[i]] == 0:
                    freqMap.pop(nums[i])
                    
                i += 1
            
            ans += j - i
        return ans
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atmost(nums, k) - self.atmost(nums, k - 1)
# Time Complexity: O(N)
# Space Complexity: O(K)


if __name__ == '__main__':
    sol = Solution()
    print(sol.subarraysWithKDistinct(nums = [1,2,1,2,3], k = 2))
    print(sol.subarraysWithKDistinct(nums = [1,2,1,3,4], k = 3))