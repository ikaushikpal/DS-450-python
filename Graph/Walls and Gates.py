# You are given a m x n 2D grid initialized with these three possible values.

# -1 : A wall or an obstacle.
# 0 : A gate.
# INF : Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a Gate, that room should remain filled with INF



# Example : 1
# Input:
# [[2147483647,-1,0,2147483647],
# [2147483647,2147483647,2147483647,-1],
# [2147483647,-1,2147483647,-1],
# [0,-1,2147483647,2147483647]]
# Output:
# [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]


# Explanation:
# the 2D grid is:
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# the answer is:
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4



# Example2
# Input:
# [[0,-1],[2147483647,2147483647]]
# Output:
# [[0,-1],[1,2]]


from typing import (
    List,
)
from collections import deque


class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        ROWS, COLS = len(rooms), len(rooms[0])
        DX = [0, 0, 1, -1]
        DY = [1, -1, 0, 0,]
        
        queue = deque()
        visited = set()

        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == 0:
                    queue.append(((i, j), 0))
                    visited.add((i, j))
        
        while queue:
            curr, dist = queue.popleft()
            rooms[curr[0]][curr[1]] = dist

            for x, y in zip(DX, DY):
                newX = curr[0] + x
                newY = curr[1] + y

                if 0<=newX<ROWS and 0<=newY<COLS and rooms[newX][newY] != -1 and (newX, newY) not in visited:
                    visited.add((newX, newY))
                    queue.append(((newX, newY), dist + 1))

        for row in rooms:
            print(*row)

if __name__ == '__main__':
    sol = Solution()
    print(sol.walls_and_gates( [[2147483647,-1,0,2147483647],
                                [2147483647,2147483647,2147483647,-1],
                                [2147483647,-1,2147483647,-1],
                                [0,-1,2147483647,2147483647]]))
