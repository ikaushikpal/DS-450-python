# Given an array containing N integers and a positive integer K, find the length of the longest sub array with sum of the elements divisible by the given value K.


# Example 1:
# Input:
# A[] = {2, 7, 6, 1, 4, 5}
# K = 3
# Output: 4
# Explanation:The subarray is {7, 6, 1, 4}
# with sum 18, which is divisible by 3.


# Example 2:
# Input:
# A[] = {-2, 2, -5, 12, -11, -1, 7}
# K = 3
# Output: 5
# Explanation:
# The subarray is {2,-5,12,-11,-1} with
# sum -3, which is divisible by 3.


class Solution:
    def longSubarrWthSumDivByK (self, arr, n, k) : 
        firstOccurrence = [None] * k
        firstOccurrence[0] = -1
        maxLength = cumSum = 0

        for i in range(n):
            cumSum += arr[i]
            rem = cumSum % k

            # only execute if there is negative nums present
            if rem < 0:
                rem += k
            if firstOccurrence[rem] is None:
                firstOccurrence[rem] = i
            else:
                length = i - firstOccurrence[rem]
                maxLength = max(maxLength, length)
        
        return maxLength
# Time Complexity: O(N)
# Space Complexity: O(K)


if __name__ == '__main__':
    sol = Solution()
    print(sol.longSubarrWthSumDivByK([2, 7, 6, 1, 4, 5], 6, 3))
    print(sol.longSubarrWthSumDivByK([-2, 2, -5, 12, -11, -1, 7], 7, 3))
    