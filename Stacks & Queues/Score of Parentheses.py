# Given a balanced parentheses string s, return the score of the string.

# The score of a balanced parentheses string is based on the following rule:

# "()" has score 1.
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
 

# Example 1:

# Input: s = "()"
# Output: 1

# Example 2:

# Input: s = "(())"
# Output: 2

# Example 3:

# Input: s = "()()"
# Output: 2


from collections import deque


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = 0
        stack = deque()
        for char in s:
            if char == '(':
                stack.append(ans)
                ans = 0
            else:
                ans = stack.pop() + max(2*ans, 1)
        return ans
# Time Complexity : O(N) where N is the length of the string.
# Space Complexity : O(N) in worst case.

    def scoreOfParentheses(self, s: str) -> int:
        depth = ans = 0
        for i, char in enumerate(s):
            if char == '(':
                depth += 1
            else:
                depth -= 1
            
            if s[i-1] == '(' and s[i] == ')':
                ans = ans + (1 << depth)
        
        return ans
# Time Complexity : O(N) where N is the length of the string.
# Space Complexity : O(1)

if __name__ == '__main__':
    sol = Solution()
    print(sol.scoreOfParentheses("(())"))
    print(sol.scoreOfParentheses("()()"))
    print(sol.scoreOfParentheses("(()(()))"))
    print(sol.scoreOfParentheses("((()))()()"))