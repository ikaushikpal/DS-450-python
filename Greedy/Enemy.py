# You live in Geek land. Geek land can be seen as a grid of shape N x M.There are K enemy at K positions. Each enemy blocks the row and column to which it belongs. You have to find the largest continuous area that is not blocked.No two enemies share the same row or the same column.


# Example 1:
# Input:
# N = 2
# M = 2
# K = 1
# enemy[]={{2,2}}
# Output:
# 1
# Explanation:
# Since only (1,1) cell is free from the enemy hence answer is 1.
 

# Example 2:
# Input:
# N = 3
# M = 3
# K = 1
# enemy[]={{3,3}}
# Output:
# 4
# Explanation:
# The cells (1,1),(1,2) ,(2,1) and (2,2) are free hence answer =4.


from typing import List


class Solution:
    def largestArea(self,n:int,m:int,k:int, enemy : List[List[int]]) -> int:
        row = [0,n+1]
        col = [0,m+1]
        
        for r,c in enemy:
            row.append(r)
            col.append(c)
            
        row.sort()
        col.sort()
        
        rmax=float('-inf')
        cmax=float('-inf')
        
        for i in range(1,len(row)):
            rmax=max(rmax,row[i]-row[i-1]-1)
            
        for i in range(1,len(col)):
            cmax=max(cmax,col[i]-col[i-1]-1)   
            
        return rmax*cmax
# Time Complexity: O(KlogK)
# Space Complexity: O(K)


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestArea(2,2,1,[[2,2]]))
    print(sol.largestArea(3,3,1,[[3,3]]))
