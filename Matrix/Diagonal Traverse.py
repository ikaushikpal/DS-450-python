# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

# Example 1:
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]


# Example 2:
# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]


from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        N, M = len(mat), len(mat[0])
        ht = {}
        for i in range(N):
            for j in range(M):
                index = i + j
                if index not in ht:
                    ht[index] = []
                ht[index].append(mat[i][j])

        ans = []
        for index in range(N + M - 1):
            if not index & 1: 
                ans.extend(reversed(ht[index]))
            else:
                ans.extend(ht[index])
        return ans
# T.C. = O(N*M)
# S.C. = O(N*M)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(sol.findDiagonalOrder([[1,2],[3,4]]))