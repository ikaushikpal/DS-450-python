# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

 
# Example 1:
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]


# Example 2:
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]


from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        queue = deque()
        visited = [[False] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    queue.append((r, c, 0))
                    visited[r][c] = True

        while queue:
            r, c, dist = queue.popleft()

            for dr, dc in MOVES:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    continue

                if visited[nr][nc]:
                    continue

                if mat[nr][nc] == 1:
                    mat[nr][nc] = dist + 1

                queue.append((nr, nc, dist + 1))
                visited[nr][nc] = True
        
        return mat


# Time Complexity: O(ROWS * COLS)
# Space Complexity: O(ROWS * COLS)


if __name__ == '__main__':
    sol = Solution()
    print(sol.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
    print(sol.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
