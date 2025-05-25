# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

# The following rules define a valid string:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "(*)"
# Output: true

# Example 3:
# Input: s = "(*))"
# Output: true
 

# Constraints:
# 1 <= s.length <= 100
# s[i] is '(', ')' or '*'.



class Solution:
    def util(self, s, index, left_count, right_count):
        if index >= len(s):
            return left_count == right_count
        
        if right_count > left_count:
            return False
        
        if (index, left_count, right_count) in self.mem:
            return self.mem[(index, left_count, right_count)]
        
        res = False
        if s[index] == '(':
            res = self.util(s, index+1, left_count+1, right_count)
        elif s[index] == ')':
            res = self.util(s, index + 1, left_count, right_count +1)
        else:
            res = self.util(s, index+1, left_count+1, right_count) or self.util(s, index + 1, left_count, right_count +1) or self.util(s, index + 1, left_count, right_count)
        self.mem[(index, left_count, right_count)] = res
        return res
        

    def checkValidString(self, s: str) -> bool:
        self.mem = {}
        return self.util(s, 0, 0, 0)


if __name__ == '__main__':
    sol = Solution()
    print(sol.checkValidString(s = "()"))
    print(sol.checkValidString(s = "(*)"))
    print(sol.checkValidString(s = "(*))"))
    print(sol.checkValidString(s = "(*)"))