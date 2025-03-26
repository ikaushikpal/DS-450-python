# You are given a n,m which means the row and column of the 2D matrix and an array of  size k denoting the number of operations. Matrix elements is 0 if there is water or 1 if there is land. Originally, the 2D matrix is all 0 which means there is no land in the matrix. The array has k operator and each operator has two integer A[i][0], A[i][1] means that you can change the cell matrix[A[i][0]][A[i][1]] from sea to island. Return how many island are there in the matrix after each operator.You need to return an array of size k.


# Example 1:
# Input: n = 4
# m = 5
# k = 4
# A = {{1,1},{0,1},{3,3},{3,4}}

# Output: 1 1 2 2
# Explanation:
# 0.  00000
#     00000
#     00000
#     00000

# 1.  00000
#     01000
#     00000
#     00000

# 2.  01000
#     01000
#     00000
#     00000

# 3.  01000
#     01000
#     00000
#     00010

# 4.  01000
#     01000
#     00000
#     00011
 

# Example 2:
# Input: n = 4
# m = 5
# k = 4
# A = {{0,0},{1,1},{2,2},{3,3}}

# Output: 1 2 3 4
# Explanation:
# 0.  00000
#     00000
#     00000
#     00000

# 1.  10000
#     00000
#     00000
#     00000

# 2.  10000
#     01000
#     00000
#     00000

# 3.  10000
#     01000
#     00100
#     00000

# 4.  10000
#     01000
#     00100
#     00010


from typing import List


class Disjoint:
    def __init__(self, n=0):
        self.n = n
        self.array = [-1] * self.n

    def add(self):
        self.array.append(-1)
        self.n += 1

    def find(self, n):
        if self.array[n] < 0:
            return (n,  -self.array[n])
        result = self.find(self.array[n])
        self.array[n] = result[0]
        return result
    
    def union(self, set1, set2):
        parent_of_set1, rank_of_set1 = self.find(set1)
        parent_of_set2, rank_of_set2 = self.find(set2)

        if parent_of_set1 == parent_of_set2:
            return False

        if rank_of_set1 > rank_of_set2:
            self.array[parent_of_set1] += self.array[parent_of_set2]
            self.array[parent_of_set2] = parent_of_set1
            
        else:
            self.array[parent_of_set2] += self.array[parent_of_set1]
            self.array[parent_of_set1] = parent_of_set2
        return True


class Solution:
    def numOfIslands(self, N: int, M : int, operators : List[List[int]]) -> List[int]:
        SEA, ISLAND = 0, 1
        MOVE_X = [0, 0, 1, -1]
        MOVE_Y = [1, -1, 0, 0]
        
        grid = [[SEA]*M for _ in range(N)]
        ans = []
        countIslands = 0
        d = Disjoint(N * M)
        
        for x, y in operators:
            if grid[x][y] == SEA:
                # following row level indexing like C 
                index = x * M + y
                
                for delX, delY in zip(MOVE_X, MOVE_Y):
                    # neighbour positioning
                    newX, newY = x + delX, y + delY
                    newIndex = newX * M + newY
                    
                    if 0 > newX or newX >= N or 0 > newY or newY >= M:
                        continue
                    
                    if grid[newX][newY] == SEA:
                        continue

                    # if neighbour is an island also disconnected from (x, y)
                    # then merging these two meaning reducing one island
                    if d.union(index, newIndex):
                        countIslands -= 1
                # if there are 4 different neighbors around (x, y) 
                # then countIslands will be decremented by 4
                # but actually we need to decremented by 3, so balancing adding 1
                countIslands += 1
            
            # adding countIslands to answer and updating cell to island in grid
            ans.append(countIslands)
            grid[x][y] = ISLAND
        return ans

# Time Complexity: O(K * 4) = O(K)
# Space Complexity: O(N * M)
# where K is length of operators; N and M is the rows and cols


if __name__ == '__main__':
    sol = Solution()
    print(sol.numOfIslands(2,4,
                            [[1, 3],
                            [0, 3],
                            [0, 1],
                            [1, 1],
                            [1, 0],
                            [1, 2],
                            [0, 3],
                            [1, 2]]))
    print(sol.numOfIslands(4, 5,
                            [[1, 1],
                            [0, 1],
                            [3, 3],
                            [3, 4]]))
    print(sol.numOfIslands(4, 5,
                            [[0, 0],
                            [1, 1],
                            [2, 2],
                            [3, 3]]))

