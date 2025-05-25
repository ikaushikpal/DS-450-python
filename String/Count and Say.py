# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

# For example, the saying and conversion for digit string "3322251":


# Given a positive integer n, return the nth term of the count-and-say sequence.

# Example 1:

# Input: n = 1
# Output: "1"
# Explanation: This is the base case.

# Example 2:

# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

class Solution:
    cache = {}

    def rle(self, s):
        value = s[0]
        freq = 1
        ans = []

        for i in range(1, len(s)):
            if value == s[i]:
                freq += 1
            else:
                ans.append(f'{freq}{value}')
                freq =  1
                value = s[i]
        ans.append(f'{freq}{value}')
        return ''.join(ans)

    def countAndSay(self, n: int) -> str:
        ans = '1'

        for i in range(1, n):
            if i not in self.cache:
                self.cache[i] = self.rle(ans)
            ans = self.cache[i]
        return ans

# Time Complexity: O(m * n) where m is the length of the output string and n is the number of iterations.
# Space Complexity: O(m) where m is the length of the output string.


if __name__ == '__main__':
    sol = Solution()
    print(sol.countAndSay(1))
    print(sol.countAndSay(2))
    print(sol.countAndSay(21))