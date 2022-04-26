# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

# Example 1:

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

# Example 2:

# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

# Example 3:

# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.

from collections import deque


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # approach:
        # 1. keep a monotonic stack of digits in increasing order
        # 2. pop until stack is empty or k is 0 if current digit is smaller than top of stack
        # 3. if k is not equals to 0, pop the top of stack until k becomes 0
        # 4. After iteration over all digits, pop all digits from stack and join them
        # 5. reverse the string [not performing here because we are using list] and remove leading zeroes, if resultant string is empty, return '0'
        # 6. return the string

        stack = []
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        if k > 0:
            stack = stack[:-k]  
            
        return "".join(stack).lstrip("0") or "0"


if __name__ == '__main__':
    num = "1432219"
    k = 3
    print(Solution().removeKdigits(num, k))

    num = "10200"
    k = 1
    print(Solution().removeKdigits(num, k))

    num = "10"
    k = 2
    print(Solution().removeKdigits(num, k))

