# You are given a string s and an integer t, representing the number of transformations to perform. In one transformation, every character in s is replaced according to the following rules:

# If the character is 'z', replace it with the string "ab".
# Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.
# Return the length of the resulting string after exactly t transformations.

# Since the answer may be very large, return it modulo 109 + 7.

# Example 1:
# Input: s = "abcyy", t = 2
# Output: 7
# Explanation:
# First Transformation (t = 1):
# 'a' becomes 'b'
# 'b' becomes 'c'
# 'c' becomes 'd'
# 'y' becomes 'z'
# 'y' becomes 'z'
# String after the first transformation: "bcdzz"
# Second Transformation (t = 2):
# 'b' becomes 'c'
# 'c' becomes 'd'
# 'd' becomes 'e'
# 'z' becomes "ab"
# 'z' becomes "ab"
# String after the second transformation: "cdeabab"
# Final Length of the string: The string is "cdeabab", which has 7 characters.

# Example 2:
# Input: s = "azbk", t = 1
# Output: 5
# Explanation:
# First Transformation (t = 1):
# 'a' becomes 'b'
# 'z' becomes "ab"
# 'b' becomes 'c'
# 'k' becomes 'l'
# String after the first transformation: "babcl"
# Final Length of the string: The string is "babcl", which has 5 characters.

# Constraints:
# 1 <= s.length <= 10^5
# s consists only of lowercase English letters.
# 1 <= t <= 10^5

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        freq = [0] * 26
        for char in s:
            idx = ord(char) - ord('a')
            freq[idx] += 1
        
        MOD = 10**9 + 7
        for _ in range(t):
            new_freq = [0] * 26

            for i in range(26):
                if i != 25: 
                    new_freq[i + 1] = (new_freq[i + 1] + freq[i]) % MOD
                else:# 'z'
                    new_freq[0] = (new_freq[0] + freq[i]) % MOD # a
                    new_freq[1] = (new_freq[1] + freq[i]) % MOD # b

            freq = new_freq
        ans = 0
        for count in freq:
            ans = (ans + count) % MOD
        return ans
# Time Complexity: O(26t)
# Space Complexity: O(26)


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthAfterTransformations(s = "abcyy", t = 2))
    print(sol.lengthAfterTransformations(s = "azbk", t = 1))




