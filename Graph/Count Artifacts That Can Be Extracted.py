from typing import List

class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        mat = [[0]*n for _ in range(n)]
        map = {}
        clock = 1

        for artifact in artifacts:
            cells = 0
            x1, y1, x2, y2 = artifact
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    cells += 1
                    mat[x][y] = clock
            
            map[clock] = cells
            clock += 1
        
        ans = 0
        for x, y in dig:
            val = mat[x][y]
            mat[x][y] = 0
            map[val] -= 1
            if map[val] == 0:
                ans += 1

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.digArtifacts(n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1]]))
    print(sol.digArtifacts(n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1],[1,1]]))


