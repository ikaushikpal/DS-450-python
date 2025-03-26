# 1. You are given a number n, representing the number of rows.
# 2. You are given a number m, representing the number of columns.
# 3. You are given n*m numbers, representing elements of 2d array a, which represents a maze.
# 4. You are standing in top-left cell and are required to move to bottom-right cell.
# 5. You are allowed to move 1 cell right (h move) or 1 cell down (v move) in 1 motion.
# 6. Each cell has a value that will have to be paid to enter that cell (even for the top-left and bottom-right cell).
# 7. You are required to traverse through the matrix and print the cost of the path which is least costly.
# 8. Also, you have to print all the paths with minimum cost.

# Input Format
# A number n
# A number m
# e11
# e12..
# e21
# e22..
# .. n * m number of elements

# Sample Input
# 6
# 6
# 0 1 4 2 8 2
# 4 3 6 5 0 4
# 1 2 4 1 4 6
# 2 0 7 3 2 2
# 3 1 5 9 2 4
# 2 7 0 8 5 1

# Sample Output
# 23
# HVVHHVHVHV
# HVVHHVHHVV

from collections import deque
from typing import List


class Solution:
    def printCostPaths(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        dx = [1, 0]
        dy = [0, 1]
        DIRS = len(dx)

        dp = [[float('inf')]*COLS for _ in range(ROWS)]
        dp[ROWS-1][COLS-1] = grid[ROWS-1][COLS-1]

        for i in range(ROWS-1, -1, -1):
            for j in range(COLS-1, -1, -1):
                for k in range(DIRS):
                    x = i + dx[k]
                    y = j + dy[k]

                    if 0<=x<ROWS and 0<=y<COLS:
                        dp[i][j] = min(dp[i][j], dp[x][y]+grid[i][j])

        print(dp[0][0])
        queue = deque([(0, 0, '')])

        while queue:
            x, y, path = queue.popleft()
            if x == ROWS-1 and y == COLS-1:
                print(path)
                continue

            if y < COLS-1:
                h_cost = dp[x][y+1]
            else:
                h_cost = float('inf')

            if x < ROWS-1:
                v_cost = dp[x+1][y]
            else: 
                v_cost = float('inf')

            if h_cost > v_cost:
                queue.append((x+1, y, f'{path}V'))
            elif h_cost < v_cost:
                queue.append((x, y+1, f'{path}H'))
            else:
                queue.append((x+1, y, f'{path}V'))
                queue.append((x, y+1, f'{path}H'))


if __name__ == '__main__':
    sol = Solution()
    sol.printCostPaths(
                    [[0, 1, 4, 2, 8, 2],
                    [4, 3, 6, 5, 0, 4],
                    [1, 2, 4, 1, 4, 6],
                    [2, 0, 7, 3, 2, 2],
                    [3, 1, 5, 9, 2, 4],
                    [2, 7, 0, 8, 5, 1],])
                
