# Find out the maximum sub-array of non negative numbers from an array.

# The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

# Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).

# Example:
# a = [1, 2, 5, -7, 2, 3]
# The two sub-arrays are [1, 2, 5] [2, 3].
# The answer is [1, 2, 5] as its sum is larger than [2, 3]

# NOTE: If there is a tie, then compare with segment's length and return segment which has maximum length.
# If there is still a tie, then return the segment with minimum starting index.
# If no such subarray is present return "-1"


# Example 1:
# Input:
# n = 3
# a[] = {1, 2, 3}
# Output: 1 2 3
# Explanation: In the given array every
# element is non-negative.


# Example 2:
# Input:
# n = 2
# a[] = {-1, 2}
# Output: 2
# Explanation: The only subarray [2] is
# the answer.


class Solution:
    def findSubarray(self, arr, n):
        finalStart = finalEnd = finalSum = finalWindowSize = 0
        start = currentSum = currentWindowSize = 0

        for i in range(n):
            if arr[i] < 0:
                currentSum = 0
                start = i + 1
                continue
            
            currentSum += arr[i]
            end = i
            currentWindowSize = end - start + 1

            if currentSum > finalSum:
                finalStart = start
                finalEnd = end
                finalSum = currentSum
                finalWindowSize = currentWindowSize

            elif currentSum == finalSum:
                if currentWindowSize > finalWindowSize:
                    finalStart = start
                    finalEnd = end
                    finalWindowSize = currentWindowSize

        if finalWindowSize == 0:
            return '-1'
        return arr[finalStart : finalEnd + 1]
# Time Complexity: O(n)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findSubarray([1, 1, -1, 2],4))
    print(sol.findSubarray([1, 2, 5, -7, 2, 3], 6))
    print(sol.findSubarray([1, 2, 3], 3))