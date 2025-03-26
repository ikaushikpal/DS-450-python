from typing import List
from functools import lru_cache


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        getMin = self.getMinInvalidParentheses(s)

        if sum(getMin) == 0:
            return [s]
        
        if sum(getMin) == len(s):
            return ['']

        self.res = set()
        self.removeInvalidParenthesesHelper(s, getMin[0], getMin[1])
        return list(self.res)
    

    def getMinInvalidParentheses(self, s):
        countLeft = countInvalid = 0

        for char in s:
            if char == '(':
                countLeft += 1
            
            if char == ')':
                if countLeft > 0:
                    countLeft -= 1
                else:
                    countInvalid += 1
        
        return (countLeft, countInvalid)
    
    def isValid(self, s):
        return sum(self.getMinInvalidParentheses(s)) == 0

    @lru_cache(None)
    def removeInvalidParenthesesHelper(self, s, l, r):
        if l == 0 and r == 0:
            if self.isValid(s):
                self.res.add(s)
            return
        
        for i in range(1, len(s)+1):
            if l > 0 and s[i-1] == '(':
                self.removeInvalidParenthesesHelper(s[:i-1] + s[i:], l-1, r)

            if r > 0 and s[i-1] == ')':
                self.removeInvalidParenthesesHelper(s[:i-1] + s[i:], l, r-1)
        

if __name__ == '__main__':
    sol = Solution()
    print(sol.removeInvalidParentheses("()())()"))
    print(sol.removeInvalidParentheses("(a)())()"))
    print(sol.removeInvalidParentheses("x("))
    print(sol.removeInvalidParentheses("((()((s((((()"))