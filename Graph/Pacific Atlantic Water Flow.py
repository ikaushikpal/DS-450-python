# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
 

# Example 1:
# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

# Example 2:
# Input: heights = [[2,1],[1,2]]
# Output: [[0,0],[0,1],[1,0],[1,1]]


from typing import List


class Solution:
    def dfs(self, x, y, visited, heights):
        ROWS, COLS = len(heights), len(heights[0])
        visited[x][y] = True
        
        for i, j in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            new_x = x + i
            new_y = y + j
            
            if 0<=new_x<ROWS and 0<=new_y<COLS and \
                heights[new_x][new_y] >= heights[x][y] and \
                not visited[new_x][new_y]:
                self.dfs(new_x, new_y, visited, heights)
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = [[False]*COLS for _ in range(ROWS)]
        atlantic = [[False]*COLS for _ in range(ROWS)]
        
        # marking first row and left most column
        # these can reach pacific
        for i in range(COLS):
            if not pacific[0][i]:
                self.dfs(0, i, pacific, heights)
        
        for i in range(ROWS):
            if not pacific[i][0]:
                self.dfs(i, 0, pacific, heights)
        
        # marking last row and right most column
        # these can reach atlantic
        for i in range(COLS):
            if not atlantic[ROWS-1][i]:
                self.dfs(ROWS-1, i, atlantic, heights)
        
        for i in range(ROWS):
            if not atlantic[i][COLS-1]:
                self.dfs(i, COLS-1, atlantic, heights)
        
        ans = []
        # finding those cells which can reach both
        for i in range(ROWS):
            for j in range(COLS):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append((i, j))
        
        return ans


if __name__ == '__main__':
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(Solution().pacificAtlantic(heights))
    heights = [[2,1],[1,2]]
    print(Solution().pacificAtlantic(heights))