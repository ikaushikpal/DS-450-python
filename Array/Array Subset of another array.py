# Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m. Task is to check whether a2[] is a subset of a1[] or not. Both the arrays can be sorted or unsorted. 
 

# Example 1:
# Input:
# a1[] = {11, 1, 13, 21, 3, 7}
# a2[] = {11, 3, 7, 1}
# Output:
# Yes
# Explanation:
# a2[] is a subset of a1[]

# Example 2:
# Input:
# a1[] = {1, 2, 3, 4, 5, 6}
# a2[] = {1, 2, 4}
# Output:
# Yes
# Explanation:
# a2[] is a subset of a1[]

# Example 3:
# Input:
# a1[] = {10, 5, 2, 23, 19}
# a2[] = {19, 5, 3}
# Output:
# No
# Explanation:
# a2[] is not a subset of a1[]


class Solution:
    def isSubset(self, a1, a2, n, m):
        a1_set = set(a1)
        a2_set = set(a2)
        return 'Yes' if a1_set.intersection(a2_set) == a2_set else 'No'
# Time Complexity: O(N)
# Space Complexity : O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.isSubset([11, 1, 13, 21, 3, 7], [11, 3, 7, 1], 6, 4))