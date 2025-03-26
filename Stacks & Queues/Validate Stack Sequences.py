# Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

# Example 1:

# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4),
# pop() -> 4,
# push(5),
# pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

# Example 2:

# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.

from collections import deque
from typing import List


class Solution:
    # my solution
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = deque()
        popped_index = 0    
        for val in pushed:
            stack.append(val)
            # poping from stack until stack is empty or popped[popped_index] is not equal to stack[-1]
            while stack and popped_index < len(popped) and stack[-1] == popped[popped_index]:
                stack.pop()
                popped_index += 1  
        # if popped sequence was correct then stack should be empty
        return len(stack) == 0
        
# Time Complexity: O(N)
# Space Complexity: O(N)

    # def validateStackSequences(self, pushed, popped):
    #     i = j = 0
    #     for x in pushed:
    #         pushed[i] = x
    #         while i >= 0 and pushed[i] == popped[j]:
    #             i, j = i - 1, j + 1
    #         i += 1
    #     return i == 0
# Time Complexity: O(N)
# Space Complexity: O(1)


if __name__ == '__main__':
    s = Solution()
    print(s.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,2,1]))
    print(s.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,3,5,1,2]))
    print(s.validateStackSequences(pushed = [1,2,3,4,5,6], popped = [4,5,3,2,6,1]))