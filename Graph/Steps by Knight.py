# Given a square chessboard, the initial position of Knight and position of a target. Find out the minimum steps a Knight will take to reach the target position.

# Note:
# The initial and the target position coordinates of Knight have been given according to 1-base indexing.

 

# Example 1:
# Input:
# N=6
# knightPos[ ] = {4, 5}
# targetPos[ ] = {1, 1}
# Output:
# 3
# Explanation:

# Knight takes 3 step to reach from 
# (4, 5) to (1, 1):
# (4, 5) -> (5, 3) -> (3, 2) -> (1, 1).
 
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function minStepToReachTarget() which takes the initial position of Knight (KnightPos), the target position of Knight (TargetPos), and the size of the chessboard (N) as input parameters and returns the minimum number of steps required by the knight to reach from its current position to the given target position.


from collections import deque


class Solution:
    def __init__(self):  
        self.xMoves = [2, 1, -1, -2, -2, -1, 1, 2]
        self.yMoves = [1, 2, 2, 1, -1, -2, -2, -1]

	#Function to find out minimum steps Knight needs to reach target position.
    def minStepToReachTarget(self, knightPos, targetPos, N):
        knightPos, targetPos = tuple(knightPos), tuple(targetPos)
        visited = set()
        queue = deque()

        queue.append((knightPos, 0)) # (position, dist)
        visited.add(knightPos)
        
        while queue:
            curr, dist = queue.popleft()
            
            if curr == targetPos:
                return dist
            
            for x, y in zip(self.xMoves, self.yMoves):
                newX = curr[0] + x
                newY = curr[1] + y

                if 1<=newX<=N and 1<=newY<=N and (newX, newY) not in visited:
                    visited.add((newX, newY))
                    queue.append(((newX, newY), dist + 1))
        
        return -1
# Time Complexity : O(N^2)
# Space Complexity : O(N^2)  


if __name__ == '__main__':
    sol = Solution()
    print(sol.minStepToReachTarget((4, 5), (1, 1), 6))