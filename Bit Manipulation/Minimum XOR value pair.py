# Given an array of integers of size N find minimum xor of any 2 elements.


# Example 1:
# Input:
# N = 3
# arr[] = {9,5,3}
# Output: 6
# Explanation: 
# There are 3 pairs -
# 9^5 = 12
# 5^3 = 6
# 9^3 = 10
# Therefore output is 6.

# Your Task:  
# You don't need to read input or print anything. Your task is to complete the function minxorpair() which takes the array arr[], its size N as input parameters and returns the minimum value of xor of any 2 elements.

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(N)

# Constraints:
# 1 <= N <= 10^5
# 1 <= arr[i] <= 10^5


class Solution:
    def minxorpair (self, N, arr):
        arr.sort()

        min_xor = float('inf')
        for i in range(N-1):
            min_xor = min(min_xor, arr[i] ^ arr[i+1])
        return min_xor
# Time Complexity: O(NlogN)
# Space Complexity: O(1)


# Optimal Approach will be Trie

if __name__ == '__main__':
    sol = Solution()
    print(sol.minxorpair(3, [9,5,3]))
        