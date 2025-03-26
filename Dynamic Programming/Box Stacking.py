# You are given a set of N types of rectangular 3-D boxes, where the ith box has height h, width w and length l. You task is to create a stack of boxes which is as tall as possible, but you can only stack a box on top of another box if the dimensions of the 2-D base of the lower box are each strictly larger than those of the 2-D base of the higher box. Of course, you can rotate a box so that any side functions as its base.It is also allowable to use multiple instances of the same type of box. You task is to complete the function maxHeight which returns the height of the highest possible stack so formed.
 

# Note: 
# Base of the lower box should be strictly larger than that of the new box we're going to place. This is in terms of both length and width, not just in terms of area. So, two boxes with same base cannot be placed one over the other.

 
# Example 1:
# Input:
# n = 4
# height[] = {4,1,4,10}
# width[] = {6,2,5,12}
# length[] = {7,3,6,32}
# Output: 60
# Explanation: One way of placing the boxes is
# as follows in the bottom to top manner:
# (Denoting the boxes in (l, w, h) manner)
# (12, 32, 10) (10, 12, 32) (6, 7, 4) 
# (5, 6, 4) (4, 5, 6) (2, 3, 1) (1, 2, 3)
# Hence, the total height of this stack is
# 10 + 32 + 4 + 4 + 6 + 1 + 3 = 60.
# No other combination of boxes produces a
# height greater than this.


# Example 2:
# Input:
# n = 3
# height[] = {1,4,3}
# width[] = {2,5,4}
# length[] = {3,6,1}
# Output: 15
# Explanation: One way of placing the boxes is
# as follows in the bottom to top manner:
# (Denoting the boxes in (l, w, h) manner)
# (5, 6, 4) (4, 5, 6) (3, 4, 1), (2, 3, 1) 
# (1, 2, 3).
# Hence, the total height of this stack is
# 4 + 6 + 1 + 1 + 3 = 15
# No other combination of boxes produces a
# height greater than this.


class Solution:
    def maxHeight(self,height, width, length, n):
        cuboids = []
        for i in range(n):
            a = height[i]
            b = width[i]
            c = length[i]
            # (width, length, height)
            cuboids.append((min(b, c), max(b, c), a))
            cuboids.append((min(a, c), max(a, c), b))
            cuboids.append((min(b, a), max(b, a), c))
        cuboids.sort()
        
        dp = [0] * len(cuboids)
        for i in range(len(cuboids)):
            dp[i] = cuboids[i][2]
            for j in range(i):
                if all(cuboids[i][k] > cuboids[j][k] for k in range(2)):
                    dp[i] = max(dp[i], cuboids[i][2] + dp[j])
        return max(dp)
# Time Complexity: O((3Nlog3N + 9N^2) = O(N^2)
# Space Complexity: O(3N) = O(N)


if __name__ == '__name__':
    sol = Solution()
    print(sol.maxHeight([4,1,4,10], [6,2,5,12], [7,3,6,32], 4))
    print(sol.maxHeight([1,4,3], [2,5,4], [3,6,1], 3))
    