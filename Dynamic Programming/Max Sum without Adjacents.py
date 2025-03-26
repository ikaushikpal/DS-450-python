# Given an array Arr of size N containing positive integers. Find the maximum sum of a subsequence such that no two numbers in the sequence should be adjacent in the array.


# Example 1:
# Input:
# N = 6
# Arr[] = {5, 5, 10, 100, 10, 5}
# Output: 110
# Explanation: If you take indices 0, 3
# and 5, then Arr[0]+Arr[3]+Arr[5] =
# 5+100+5 = 110.
 

# Example 2:
# Input:
# N = 4
# Arr[] = {3, 2, 7, 10}
# Output: 13
# Explanation: 3 and 10 forms a non
# continuous  subsequence with maximum
# sum.

class Solution:
    def findMaxSum(self,arr, n):
        if n == 1:
            return arr[0]

        prevPrevMax = arr[0]
        prevMax = arr[1]
        ans = max(prevMax, prevPrevMax)

        for i in range(2, n):
            curr = arr[i] + prevPrevMax
            ans = max(ans, curr)
            prevPrevMax = max(prevPrevMax, prevMax)
            prevMax = max(prevMax, curr)
        return ans
# Time Complexity: O(N)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaxSum([5, 5, 10, 100, 10, 5], 6))
    print(sol.findMaxSum([3, 2, 7, 10], 4))