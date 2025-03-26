# Given an unsorted array arr[ ] of size n, you need to find the maximum difference of absolute values of elements and indexes, i.e., for i <= j, calculate maximum of | arr[ i ] - arr[ j ] | + | i - j |. 


# Example 1:
# Input : 
# n = 3
# arr[ ] = {1, 3, -1}
# Output: 5
# Explanation:
# Maximum difference comes from indexes 
# 1, 2 i.e | 3 - (-1) | + | 1 - 2 | = 5

# Example 2:
# Input : 
# n = 4
# arr[ ] = {5, 9, 2, 6} 
# Output:  8
# Explanation: 
# Maximum difference comes from indexes 
# 1, 2 i.e | 9 - 2 | + | 1 - 2 | = 8


class Solution:
    def maxDistance (self, arr, n):
        # to solve this problem we need to find two equations
        # given condition is | arr[ i ] - arr[ j ] | + | i - j |
        # we can write this as
        # | arr[ i ] - arr[ j ] | + j - i; given i <= j
        #         term1            + term2
        # we are using absolute value, so either term1 will be positive initial
        # and term1 can be negative and it will become positive

        # CASE1: term1 is positive
        # meaning arr[ i ] > arr[ j ] 
        # so we can write this as
        # (arr[ i ] - arr[ j ]) + j - i
        # = arr[ i ] - i + j - arr[ j ]
        # = (arr[ i ] - i) + (j - arr[ j ])
        # = (arr[ i ] - i) - (arr[ j ] - j)
        # so we need to compute (arr[i] - i) and storing maximum one
        # denoting as maxx

        # CASE2: term1 is negative
        # meaning arr[ i ] < arr[ j ]
        # so we can write this as
        # (arr[ j ] - arr[ i ]) + j - i
        # = arr[ j ] + j - i - arr[ i ]
        # = (arr[ j ] + j) + (-i - arr[ i ])
        # = (arr[ j ] + j) - (arr[ i ] + i)
        # so we need to compute (arr[i] + i) and storing minimum one
        # denoting as minn
        ans = 0
        maxx = minn = arr[0]

        for i in range(n):
            newMaxx = arr[i] - i
            newMinn = arr[i] + i

            ans = max(ans, maxx - newMaxx, newMinn - minn)
            maxx = max(maxx, newMaxx)
            minn = min(minn, newMinn)
        return ans
# Time Complexity: O(n)
# Auxiliary Space: O(1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxDistance([1, 3, -1], 3))
    print(sol.maxDistance([5, 9, 2, 6], 4))

