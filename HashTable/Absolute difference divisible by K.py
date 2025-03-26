# Given an array of integers of size n and an integer k, find all the pairs in the array whose absolute difference is divisible by k.


# Example 1:
# Input:
# n = 3
# arr[] = {3, 7, 11}
# k = 4
# Output:
# 3
# Explanation:
# (11-3) = 8 is divisible by 4
# (11-7) = 4 is divisible by 4
# (7-3) = 4 is divisible by 4


# Example 2:
# Input:
# n = 4
# arr[] = {1, 2, 3, 4}
# k = 2
# Output :
# 2
# Explanation:
# Valid pairs are (1,3), and (2,4).


class Solution:
    def countPairs (self, n, arr, k):
        rem = [0] * k
        for val in arr:
            rem[val % k] += 1
        
        ans = 0
        for i in range(k):
            ans += ((rem[i] - 1) * rem[i]) >> 1
        return ans
# Time Complexity: O(n)
# Space Complexity: O(k)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countPairs(3, [3, 7, 11], 4))
    print(sol.countPairs(4, [1, 2, 3, 4], 2))