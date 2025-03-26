# Given an array A[ ] of N of  integers, find the index of values that satisfy A + B = C + D where A,B,C & D are integers values in the array.
# Note: As there may be multiple pairs satisfying the equation return lexicographically smallest order of  A, B, C and D and return all as -1 if there are no pairs satisfying the equation.

 
# Example 1:
# Input:
# N = 7
# A[] = {3, 4, 7, 1, 2, 9, 8}
# Output:
# 0 2 3 5
# Explanation:
# A[0] + A[2] = 3+7 = 10
# A[3] + A[5] = 1+9 = 10


# Example 2:
# Input:
# N = 4
# A[] = {424, 12, 31, 7}
# Output:
# -1 -1 -1 -1
# Explanation:
# There are no pairs satisfying the equation.


class Solution:
    def satisfyEqn(self, A, N):
        uniqueSubset = {}
        ans = (N+1, N+1, N+1, N+1)
        
        for i in range(N):
            for j in range(i+1, N):
                tot = A[i] + A[j]
                
                if tot in uniqueSubset:
                    if i not in uniqueSubset[tot] and j not in uniqueSubset[tot]:
                        temp = (*uniqueSubset[tot], i, j)
                        ans = min(ans, temp)
                else:
                    uniqueSubset[tot] = (i, j)
                
        if ans == (N+1, N+1, N+1, N+1):
            return (-1, -1, -1, -1)
        return ans
# Time Complexity: O(N^2)
# Space Complexity: O(N^2)


if __name__ == '__main__':
    sol = Solution()
    print(sol.satisfyEqn([3, 4, 7, 1, 2, 9, 8], 7))
    print(sol.satisfyEqn([424, 12, 31, 7], 4))