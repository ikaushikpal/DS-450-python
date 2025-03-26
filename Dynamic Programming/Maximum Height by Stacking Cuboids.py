# Given n cuboids where the dimensions of the ith cuboid is cuboids[i] = [widthi, lengthi, heighti] (0-indexed). Choose a subset of cuboids and place them on each other.

# You can place cuboid i on cuboid j if widthi <= widthj and lengthi <= lengthj and heighti <= heightj. You can rearrange any cuboid's dimensions by rotating it to put it on another cuboid.

# Return the maximum height of the stacked cuboids.

 
# Example 1:
# Input: cuboids = [[50,45,20],[95,37,53],[45,23,12]]
# Output: 190
# Explanation:
# Cuboid 1 is placed on the bottom with the 53x37 side facing down with height 95.
# Cuboid 0 is placed next with the 45x20 side facing down with height 50.
# Cuboid 2 is placed next with the 23x12 side facing down with height 45.
# The total height is 95 + 50 + 45 = 190.


# Example 2:
# Input: cuboids = [[38,25,45],[76,35,3]]
# Output: 76
# Explanation:
# You can't place any of the cuboids on the other.
# We choose cuboid 1 and rotate it so that the 35x3 side is facing down and its height is 76.


# Example 3:
# Input: cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]
# Output: 102
# Explanation:
# After rearranging the cuboids, you can see that all cuboids have the same dimension.
# You can place the 11x7 side down on all cuboids so their heights are 17.
# The maximum height of stacked cuboids is 6 * 17 = 102.


from typing import List


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        N = len(cuboids)
        for i in range(N):
            # (width, length, height)
            # in greedy manner choosing the largest side as height
            cuboids[i].sort()
        cuboids.sort()
        
        dp = [0] * N
        for i in range(N):
            dp[i] = cuboids[i][2]
            for j in range(i):
                if all(cuboids[i][k] >= cuboids[j][k] for k in range(3)):
                    dp[i] = max(dp[i], cuboids[i][2] + dp[j])
        return max(dp)
# Time Complexity: O(NlogN + N^2) = O(N^2)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxHeight([[50,45,20],[95,37,53],[45,23,12]]))
    print(sol.maxHeight([[38,25,45],[76,35,3]]))
    print(sol.maxHeight([[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]))