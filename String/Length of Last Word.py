# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

 
# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.


# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.


# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        
        # skipping spaces
        while i >= 0 and s[i].isspace():
            i -= 1
        
        ans = 0
        while i >= 0 and not s[i].isspace():
            ans += 1
            i -= 1
        return ans
# Time Complexity: O(N)
# Space Complexity : O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLastWord(s = "Hello World"))
    print(sol.lengthOfLastWord(s = "   fly me   to   the moon  "))
    print(sol.lengthOfLastWord(s = "luffy is still joyboy"))