# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

# A subarray is a contiguous part of an array.

 

# Example 1:
# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]


# Example 2:
# Input: nums = [5], k = 9
# Output: 0


from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        occurrence = [0] * k
        occurrence[0] = 1
        count = cumSum = 0

        for num in nums:
            cumSum += num
            rem = cumSum % k

            # only execute if there is negative nums present
            if rem < 0:
                rem += k

            count += occurrence[rem]
            occurrence[rem] += 1
        
        return count
# Time Complexity: O(N)
# Space Complexity: O(K)


if __name__ == '__main__':
    sol = Solution()
    print(sol.subarraysDivByK([4,5,0,-2,-3,1], 5))
    print(sol.subarraysDivByK([5], 9))