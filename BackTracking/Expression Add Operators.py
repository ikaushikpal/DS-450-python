# Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

# Note that operands in the returned expressions should not contain leading zeros.


# Example 1:
# Input: num = "123", target = 6
# Output: ["1*2*3","1+2+3"]
# Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.


# Example 2:
# Input: num = "232", target = 8
# Output: ["2*3+2","2+3*2"]
# Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.


# Example 3:
# Input: num = "3456237490", target = 9191
# Output: []
# Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.


from typing import List


class Solution:
    def dfs(self, expr='', i=0, evalSoFar=0, prevNum=0):
        if i == len(self.num):
            if evalSoFar == self.target:
                self.ans.append(expr)
            return
        
        num, numStr = 0, ''
        for j in range(i, len(self.num)):
            # no leading zero is allowed but '0' is allowed
            if j > i and self.num[i] == '0':
                break

            num = num * 10 + int(self.num[j])
            numStr += self.num[j]
            
            if i == 0:
                self.dfs(numStr, j+1, num, num)
            else:
                self.dfs(expr + '+' + numStr, j+1, evalSoFar + num, num)
                self.dfs(expr + '-' + numStr, j+1, evalSoFar - num, -num)
                self.dfs(expr + '*' + numStr, j+1, evalSoFar - prevNum + prevNum * num, prevNum * num)

    def addOperators(self, num: str, target: int) -> List[str]:
        self.num = num
        self.target = target
        self.ans = []
        self.dfs()
        return self.ans
# Time Complexity: O(4^n) [+, -, *, no-skip]
# Space Complexity: O(4^n)


if __name__ == '__main__':
    sol = Solution()
    print(sol.addOperators(num="105", target=5))
    print(sol.addOperators("123", 6))
    print(sol.addOperators(num = "232", target = 8))
    print(sol.addOperators("3456237490", 9191))