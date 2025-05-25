# You are given a string s that consists of lower case English letters and brackets.

# Reverse the strings in each pair of matching parentheses, starting from the innermost one.

# Your result should not contain any brackets.

 
# Example 1:
# Input: s = "(abcd)"
# Output: "dcba"

# Example 2:
# Input: s = "(u(love)i)"
# Output: "iloveu"
# Explanation: The substring "love" is reversed first, then the whole string is reversed.

# Example 3:
# Input: s = "(ed(et(oc))el)"
# Output: "leetcode"
# Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
 

# Constraints:
# 1 <= s.length <= 2000
# s only contains lower case English characters and parentheses.
# It is guaranteed that all parentheses are balanced.


from collections import deque


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ')':
                portions = []
                while stack and stack[-1] != '(':
                    portions.append(stack.pop())
                stack.pop()
                stack.extend(portions)
            else:
                stack.append(c)
        return ''.join(stack)
# Time Complexity: O(N^2)
# Space Complexity: O(N)



if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseParentheses(s = "(abcd)"))
    print(sol.reverseParentheses(s = "(u(love)i)"))
    print(sol.reverseParentheses(s = "(ed(et(oc))el)"))



