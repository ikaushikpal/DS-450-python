# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2


# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2


from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        ans = total = 0
        
        for num in nums:
            total += num
            req = total - k
            
            if req in freq:
                ans += freq[req]
            
            if total not in freq:
                freq[total] = 1
            else:
                freq[total] += 1
        
        return ans
# Time Complexity: O(N)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.subarraySum([1,1,1], 2))
    print(sol.subarraySum([1,2,3], 3))