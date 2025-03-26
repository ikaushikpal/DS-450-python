# One day Jim came across array arr[] of N numbers. He decided to divide these N numbers into different groups. Each group contains numbers in which sum of any two numbers should not be divisible by an integer K. Print the size of the group containing maximum numbers.


# Example 1:
# Input:
# N = 4, K = 8
# arr[] = {1, 7, 2, 6}
# Output:
# 2
# Explanation:
# The  group of numbers which can be formed
# are: (1),(2),(7),(6),(1,2),(1,6),(7,2),(7,6).
# So,the maximum possible size of the group is 2.


# Example 2:
# Input:
# N = 2, K = 3
# arr[] = {1, 2}
# Output:
# 1
# Explanation:
# The  group of numbers which can be formed
# are: (1),(2). So,the maximum possible size
# of the group is 1.



from collections import defaultdict


class Solution:
    def maxGroupSize(self, arr, N, K):
        remMap = defaultdict(int)
        for val in arr:
            rem = val % K
            remMap[rem] += 1
        
        ans = 0
        for rem in range(K//2 + 1):
            if rem == 0 or rem * 2 == K:
                ans += min(1, remMap[rem])
            else:
                ans += max(remMap[rem], remMap[K - rem])
        return ans
# Time Complexity: O(N)
# Space Complexity: O(K)


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxGroupSize([1, 7, 2, 6], 4, 8))
    print(sol.maxGroupSize([1, 2], 2, 3))
    