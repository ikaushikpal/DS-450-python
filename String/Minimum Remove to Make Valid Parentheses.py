# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
 

# Example 1:

# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

# Example 2:

# Input: s = "a)b(c)d"
# Output: "ab(c)d"

# Example 3:

# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.


from collections import deque


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = deque()
        opened = 0

        for c in s:
            if c == '(':
                opened += 1
            elif c == ')':
                if opened <= 0: continue
                opened -= 1
            stack.append(c)
        
        opened = 0
        ans = []
        while stack:
            c = stack.pop()

            if c == ')':
                opened -= 1
            elif c == '(':
                if opened >= 0: continue
                opened += 1
            ans.append(c)

        return ''.join(ans[::-1])
# Time Complexity: O(N)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minRemoveToMakeValid("lee(t(c)o)de)"))
    print(sol.minRemoveToMakeValid("a)b(c)d"))
    print(sol.minRemoveToMakeValid("))(("))