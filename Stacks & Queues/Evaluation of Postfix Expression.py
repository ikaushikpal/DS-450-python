from collections import deque


class Solution:
    
    #Function to evaluate a postfix expression.
    def EvaluatePostfix(self, S):
        stack = deque()
        
        for char in S:
            if char.isdigit():
                stack.append(int(char))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                # *, /, + and -.
                if char == '*':
                    stack.append(op1 * op2)
                elif char == '/':
                    stack.append(op1 // op2)
                elif char == '-':
                    stack.append(op1 - op2)
                else:
                    stack.append(op1 + op2)
        return stack.pop()
        