# Given a matrix as 2D array. Find the reverse spiral traversal of the matrix. 

# Example 1:
# Input: R = 3, C = 3
#   a = {{9, 8, 7},
#        {6, 5, 4},
#        {3, 2, 1}}
# Output: 5 6 3 2 1 4 7 8 9
# Explanation: Spiral form of the matrix
# in reverse order starts from the centre 
# and goes outward.



# Example 2:
# Input: R = 4, C = 4 
#   a = {{1, 2, 3, 4},
#        {5, 6, 7, 8},
#        {9, 10, 11, 12}, 
#        {13, 14, 15, 16}}
# Output: 10 11 7 6 5 9 13 14 15 16 12 8 4 3 2 1
# Explanation: 


class Solution:
    def reverseSpiral(self, R, C, A):
        iMin = jMin = 0
        iMax, jMax = len(A)-1, len(A[0])-1
        remaining = R * C
        ans = []
        
        while iMin <= iMax and jMin <= jMax:
            for j in range(jMin, jMax + 1):
                if remaining > 0:
                    ans.append(A[iMin][j])
                    remaining -= 1
            iMin += 1
            
            for i in range(iMin, iMax + 1):
                if remaining > 0:
                    ans.append(A[i][jMax])
                    remaining -= 1
            jMax -= 1
            
            for j in range(jMax, jMin - 1, -1):
                if remaining > 0:
                    ans.append(A[iMax][j])
                    remaining -= 1
            iMax -= 1
            
            for i in range(iMax, iMin - 1, -1):
                if remaining > 0:
                    ans.append(A[i][jMin])
                    remaining -= 1
            jMin += 1
        return ans[::-1]
# Time Complexity: O(R * C)
# Space Complexity: O(R * C)


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseSpiral(3, 3, [[9, 8, 7], [6, 5, 4], [3, 2, 1]]))
    print(sol.reverseSpiral(4, 4, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
