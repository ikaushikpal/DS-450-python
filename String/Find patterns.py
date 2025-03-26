# Given two strings S and W. Find the number of times W appears as a subsequence of string S where every character of string S can be included in forming at most one subsequence.
 
# Example 1:
# Input: 
#  S = "abcdrtbwerrcokokokd" 
#  W = "bcd" 
# Output: 
#  2
# Explanation: 
# The two subsequences of string W are
# { S1 , S2 , S3 } and { S6 , S11 , S18 }
# (Assuming 0- based indexing).
 

# Example 2:
# Input: 
# S = "ascfret" 
# W = "qwer" 
# Output: 
# 0
# Explanation:
# No valid subsequences are possible.


class Solution:
    def numberOfSubsequences(self, S, W):
        S = list(S)
        ans = i = j = 0
        
        while i < len(S):
            if S[i] == W[j]:
                S[i] = '$'
                j += 1
                
            if j == len(W):
                ans += 1
                j = i = 0
            else:
                i += 1
        return ans
# Time Complexity: O(N^2)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfSubsequences("abcdrtbwerrcokokokd", "bcd"))
    print(sol.numberOfSubsequences("ascfret", "qwer"))
