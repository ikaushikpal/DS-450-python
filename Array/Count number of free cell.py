# Given a Matrix size N*N and an integer K. Initially, the matrix contains only 0. You are given K tasks and for each task, you are given two coordinates (r,c) [1 based index]. Where coordinates (r,c) denotes rth row and cth column of the given matrix.

# You have to perform each task sequentially in the given order. For each task, You have to put 1 in all rth row cells and all cth columns cells.

# After each task, You have to calculate the number of 0 present in the matrix and return it.



# Example 1:
# Input:
# n = 3, k= 3
# 2 2
# 2 3
# 3 2
# Output: 4 2 1
# Explanation: 
# After 1st Operation, all the 2nd row
# and all the 2nd column will be filled by
# 1. So remaning cell with value 0 will be 4
# After 2nd Operation, all the 2nd row and all
# the 3rd column will be filled by 1. So 
# remaning cell with value 0 will be 2.
# After 3rd Operation cells having value 0 will
# be 1.


# Example 2:
# Input:
# n = 2, k = 2
# 1 2
# 1 1
# Output: 1 0
# Explanation: 
# After 1st Operation, all the 1st row and 
# all the 2nd column will be filled by 1. 
# So remaning cell with value 0 will be 1.
# After 2nd Operation, all the 1st row and 
# all the 1st column will be filled by 1. 
# So remaning cell with value 0 will be 0. 


class Solution():
    def countZero(self, n, k ,arr):
        rows = [False] * n
        cols = [False] * n
        countZeros = n * n
        countRowOnes = countColOnes = 0
        
        ans = []
        for i, j in arr:
            if rows[i - 1] == False:
                countZeros -= n - countColOnes
                rows[i - 1] = True
                countRowOnes += 1
            
            if cols[j - 1] == False:
                countZeros -= n - countRowOnes
                cols[j - 1] = True
                countColOnes += 1
            
            ans.append(countZeros)
        return ans
# Time Complexity: O(k)
# Space Complexity: O(max(n, k))


if __name__ == '__main__':
    sol = Solution()
    print(sol.countZero(3, 3, [[2, 2], [2, 3], [3, 2]]))
    print(sol.countZero(2, 2, [[1, 2], [1, 1]]))