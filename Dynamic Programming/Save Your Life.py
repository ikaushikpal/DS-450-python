# Given a string w, integer array b,  character array x and an integer n. n is the size of array b and array x. Find a substring which has the sum of the ASCII values of its every character, as maximum. ASCII values of some characters are redefined.
# Note: Uppercase & lowercase both will be present in the string w. Array b and Array x contain corresponding redefined ASCII values. For each i, 0<=ib[i] contain redefined ASCII value of character x[i].


# Example 1:
# Input:
# W = abcde
# N = 1
# X[] = { 'c' }
# B[] = { -1000 }
# Output:
# de
# Explanation:
# Substring "de" has the
# maximum sum of ascii value,
# including c decreases the sum value


# Example 2:
# Input:
# W = dbfbsdbf 
# N = 2
# X[] = { 'b','s' }
# B[] = { -100, 45  }
# Output:
# dbfbsdbf
# Explanation:
# Substring "dbfbsdbf" has the maximum
# sum of ascii value.


class Solution:
    def maxSum (self, w, x, b, n):
        newCharMap = {char:value for char, value in zip(x, b)}
        finalStart = finalEnd = -1
        start = 0
        maxScore, currentScore = float('-inf'), 0
        
        for end, char in enumerate(w):
            currentScore += newCharMap.get(char, ord(char))
            
            if maxScore < currentScore:
                maxScore = currentScore
                finalStart = start
                finalEnd = end
                
            if currentScore < 0:
                currentScore = 0
                start = end + 1       
        return w[finalStart : finalEnd + 1]
# Variation of Kadane Algorithm
# Time Complexity: O(|W|)
# Space Complexity: O(256) = O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSum('abcde', ['c'], [-1000], 1))
    print(sol.maxSum('dbfbsdbf', ['b', 's'], [-100, 45], 2))