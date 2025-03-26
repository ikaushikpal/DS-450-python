# You are given a string s consisting of only lowercase English letters. In one operation, you can:

# Delete the entire string s, or
# Delete the first i letters of s if the first i letters of s are equal to the following i letters in s, for any i in the range 1 <= i <= s.length / 2.
# For example, if s = "ababc", then in one operation, you could delete the first two letters of s to get "abc", since the first two letters of s and the following two letters of s are both equal to "ab".

# Return the maximum number of operations needed to delete all of s.


# Example 1:
# Input: s = "abcabcdabc"
# Output: 2
# Explanation:
# - Delete the first 3 letters ("abc") since the next 3 letters are equal. Now, s = "abcdabc".
# - Delete all the letters.
# We used 2 operations so return 2. It can be proven that 2 is the maximum number of operations needed.
# Note that in the second operation we cannot delete "abc" again because the next occurrence of "abc" does not happen in the next 3 letters.


# Example 2:
# Input: s = "aaabaab"
# Output: 4
# Explanation:
# - Delete the first letter ("a") since the next letter is equal. Now, s = "aabaab".
# - Delete the first 3 letters ("aab") since the next 3 letters are equal. Now, s = "aab".
# - Delete the first letter ("a") since the next letter is equal. Now, s = "ab".
# - Delete all the letters.
# We used 4 operations so return 4. It can be proven that 4 is the maximum number of operations needed.


# Example 3:
# Input: s = "aaaaa"
# Output: 5
# Explanation: In each operation, we can delete the first letter of s.



class Solution:
    def helper(self, index, length):
        if index >= length:
            return 0
        
        if self.dp[index] != -1:
            return self.dp[index]
        
        res = 1
        for i in range(1, length):
            l1, r1 = index, index + i - 1
            l2, r2 = r1 + 1, r1 + i

            if r2 >= length:
                break

            if self.compareHash(l1, r1, l2, r2):
                res = max(res, 1 + self.helper(r1 + 1, length))  

        self.dp[index] = res
        return res

    def computeHash(self, s):
        N = len(s)
        BASE = 29
        hashTable = [[0]*N for _ in range(N)]

        for i in range(N):
            hashValue = 0
            power = BASE
            for j in range(i, N):
                charValue = ord(s[j]) - ord('a') + 1
                hashValue += power * charValue
                power *= BASE
                hashTable[i][j] = hashValue
        return hashTable

    def compareHash(self, l1, r1, l2, r2):
        return self.hashTable[l1][r1] == self.hashTable[l2][r2]

    def deleteString(self, s: str) -> int:
        self.dp = [-1] * len(s)
        self.hashTable = self.computeHash(s)
        return self.helper(0, len(s))


if __name__ == '__main__':
    sol = Solution()
    print(sol.deleteString("abcabcdabc"))
    print(sol.deleteString("aaabaab"))
    print(sol.deleteString("aaaaa"))