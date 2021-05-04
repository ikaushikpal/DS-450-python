from collections import deque


class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self, string):
        stack = deque()

        for char in string:
            if char == '(' or char == '{'or char == '[':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False

                if stack[-1] == '(' and char == ')':
                    stack.pop()
                elif stack[-1] == '{' and char == '}':
                    stack.pop()
                elif stack[-1] == '[' and char == ']':
                    stack.pop()
                
                else:
                    return False
        
        if len(stack) == 0:
            return True
        return False