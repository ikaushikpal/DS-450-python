# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

 

# Example 1:
# Input: s = "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

# Example 2:
# Input: s = "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation: 
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

# Example 3:
# Input: s = "()()"
# Output: ""
# Explanation: 
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".
 

# Constraints:
# 1 <= s.length <= 10^5
# s[i] is either '(' or ')'.
# s is a valid parentheses string.


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        left_params = 0

        for c in s:
            # only adding left bracket if depth is 1 or more
            # () then left_params = 0 then dont add
            # (()) here left_params = 1 > 0 add
            if c == '(' and left_params > 0:
                res.append('(')
            
            # same with ')' logic just reverse
            # only pop if count is > 1
            # () here dont need to pop
            # (()) here need to cause ((
            if c == ')' and left_params > 1:
                res.append(')')
            
            if c == '(':
                left_params += 1
            else:
                left_params -= 1
        return ''.join(res)
# Time Complexity: O(N)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeOuterParentheses(s = "(()())(())"))
    print(sol.removeOuterParentheses(s = "(()())(())(()(()))"))
    print(sol.removeOuterParentheses(s = "()()"))