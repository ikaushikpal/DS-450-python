# Given an array containing 0s and 1s. Find the number of subarrays having equal number of 0s and 1s.

# Example 1:
# Input:
# n = 7
# A[] = {1,0,0,1,0,1,1}
# Output: 8
# Explanation: The index range for the 8 
# sub-arrays are: (0, 1), (2, 3), (0, 3), (3, 4), 
# (4, 5) ,(2, 5), (0, 5), (1, 6)


# Example 2:
# Input:
# n = 5
# A[] = {1,1,1,1,0}
# Output: 1
# Explanation: The index range for the 
# subarray is (3,4).



class Solution:
    def countSubSumZero(self, nums):
        prefixMap = {}
        prefixMap[0] = 1
        count = cumSum = 0

        for num in nums:
            cumSum += num
            if cumSum not in prefixMap:
                prefixMap[cumSum] = 1
            else:
                count += prefixMap[cumSum]
                prefixMap[cumSum] += 1

        return count
    def countSubarrWithEqualZeroAndOne(self, nums, n):
        # the trick is that map 0 to -1 and keep 1 to 1
        # then simply find maximum sub-array of sum == 0
        for i, num in enumerate(nums):
            if num == 0:
                nums[i] = -1
        return self.countSubSumZero(nums)
# Time Complexity: O(N)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countSubarrWithEqualZeroAndOne([1, 0, 0, 1, 0, 1, 1], 7))
    print(sol.countSubarrWithEqualZeroAndOne([1, 1, 1, 1, 0], 5))