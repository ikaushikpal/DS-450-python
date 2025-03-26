# There is a row of N houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color. Find the minimum cost to paint all houses.

# The cost of painting each house in red, blue or green colour is given in the array r[], g[] and b[] respectively.


# Example 1:
# Input:
# N = 3
# r[] = {1, 1, 1}
# g[] = {2, 2, 2}
# b[] = {3, 3, 3}
# Output: 4
# Explanation: We can color the houses 
# in RGR manner to incur minimum cost.
# We could have obtained a cost of 3 if 
# we coloured all houses red, but we 
# cannot color adjacent houses with 
# the same color.


# Example 2:
# Input:
# N = 3
# r[] = {2, 1, 3}
# g[] = {3, 2, 1}
# b[] = {1, 3, 2} 
# Output: 3
# Explanation: We can color the houses
# in BRG manner to incur minimum cost.


class Solution:
    def distinctColoring (self, N, r, g, b):
        for i in range(1, len(r)):
            r[i] += min(g[i - 1], b[i - 1])
            g[i] += min(r[i - 1], b[i - 1])
            b[i] += min(r[i - 1], g[i - 1])
            
        return min(r[-1], g[-1], b[-1])
# Time Complexity: O(N)
# Space Complexity: O(1)

if __name__ == '__main__':
    sol = Solution()
    print(sol.distinctColoring(3, [1, 1, 1], [2, 2, 2], [3, 3, 3]))
    