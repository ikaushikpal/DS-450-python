from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M, N = len(matrix), len(matrix[0])
        
        ans = []
        up = left = 0
        right, down = N - 1, M - 1
        
        while up <= down and left <= right:
            for j in range(left, right + 1):
                if len(ans) < M * N:
                    ans.append(matrix[up][j])
            up += 1
            
            for i in range(up, down + 1):
                if len(ans) < M * N:
                    ans.append(matrix[i][right])
            right -= 1
            
            for j in range(right, left-1, -1):
                if len(ans) < M * N:
                    ans.append(matrix[down][j])
            down -= 1
            
            for i in range(down, up-1, -1):
                if len(ans) < M * N:
                    ans.append(matrix[i][left])
            left += 1
        return ans
    

sol = Solution()
print(sol.spiralOrder([[6,9,7]]))