# You are given a string s consisting of lowercase English letters, an integer t representing the number of transformations to perform, and an array nums of size 26. In one transformation, every character in s is replaced according to the following rules:

# Replace s[i] with the next nums[s[i] - 'a'] consecutive characters in the alphabet. For example, if s[i] = 'a' and nums[0] = 3, the character 'a' transforms into the next 3 consecutive characters ahead of it, which results in "bcd".
# The transformation wraps around the alphabet if it exceeds 'z'. For example, if s[i] = 'y' and nums[24] = 3, the character 'y' transforms into the next 3 consecutive characters ahead of it, which results in "zab".
# Return the length of the resulting string after exactly t transformations.

# Since the answer may be very large, return it modulo 109 + 7.

 
# Example 1:
# Input: s = "abcyy", t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]

# Output: 7

# Explanation:
# First Transformation (t = 1):

# 'a' becomes 'b' as nums[0] == 1
# 'b' becomes 'c' as nums[1] == 1
# 'c' becomes 'd' as nums[2] == 1
# 'y' becomes 'z' as nums[24] == 1
# 'y' becomes 'z' as nums[24] == 1
# String after the first transformation: "bcdzz"
# Second Transformation (t = 2):

# 'b' becomes 'c' as nums[1] == 1
# 'c' becomes 'd' as nums[2] == 1
# 'd' becomes 'e' as nums[3] == 1
# 'z' becomes 'ab' as nums[25] == 2
# 'z' becomes 'ab' as nums[25] == 2
# String after the second transformation: "cdeabab"
# Final Length of the string: The string is "cdeabab", which has 7 characters.

# Example 2:
# Input: s = "azbk", t = 1, nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
# Output: 8

# Explanation:
# First Transformation (t = 1):
# 'a' becomes 'bc' as nums[0] == 2
# 'z' becomes 'ab' as nums[25] == 2
# 'b' becomes 'cd' as nums[1] == 2
# 'k' becomes 'lm' as nums[10] == 2
# String after the first transformation: "bcabcdlm"
# Final Length of the string: The string is "bcabcdlm", which has 8 characters.


# Constraints:
# 1 <= s.length <= 10^5
# s consists only of lowercase English letters.
# 1 <= t <= 10^9
# nums.length == 26
# 1 <= nums[i] <= 25


from typing import List

class Solution:
    def matrixMultiply(self, matrixA, matrixB):
        MOD = 10**9 + 7
        rowA, colA = len(matrixA), len(matrixA[0])
        rowB, colB = len(matrixB), len(matrixB[0])

        if colA != rowB:
            return None

        matrixC = [[0] * colB for _ in range(rowA)]
        for i in range(rowA):
            for j in range(colB):
                for k in range(colA):
                    matrixC[i][j] = (matrixC[i][j] + (matrixA[i][k] * matrixB[k][j]) % MOD) % MOD
        
        return matrixC

    def matrixExponential(self, matrix, power):
        row, col = len(matrix), len(matrix[0])

        identityMatrix = [[0]*col for _ in range(col)]
        for i in range(col):
            identityMatrix[i][i] = 1
        
        res = identityMatrix
        while power > 0:
            if power & 1:
                res = self.matrixMultiply(res, matrix)  # Note: res * matrix, not matrix * res
            
            matrix = self.matrixMultiply(matrix, matrix)
            power = power >> 1
        return res
    
    def generateTransformMatrix(self, nums):
        # Create a 26x26 matrix where matrix[i][j] = 1 if character i transforms to j
        matrix = [[0]*26 for _ in range(26)]
        for i in range(26):
            for j in range(1, nums[i]+1):
                idx = (i + j) % 26
                matrix[i][idx] += 1
        return matrix
    
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 10**9 + 7

        # Initialize the frequency vector (1x26)
        freq = [0] * 26
        for char in s:
            idx = ord(char) - ord('a')
            freq[idx] += 1

        # Generate transformation matrix
        transform_matrix = self.generateTransformMatrix(nums)
        
        # Compute the matrix exponentiation
        transform_matrix_pow = self.matrixExponential(transform_matrix, t)
        
        # Multiply the frequency vector with the transformation matrix
        result = 0
        for i in range(26):
            for j in range(26):
                result = (result + freq[i] * transform_matrix_pow[i][j]) % MOD
        
        return result
# TIme Complexity: O(26^3logt)
# Space Complexity: O(26^3)


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthAfterTransformations(s = "abcyy", t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]))
    print(sol.lengthAfterTransformations(s = "azbk", t = 1, nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]))