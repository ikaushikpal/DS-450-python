# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 

# Example 1:
# Input: columnNumber = 1
# Output: "A"


# Example 2:
# Input: columnNumber = 28
# Output: "AB"


# Example 3:
# Input: columnNumber = 701
# Output: "ZY"


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # ALGO
        # Equation relationships will help us through the process, and It it not very difficult to derive them. With equations we can understand how to get the n-1 at first of the loop.
        # The relationship between the string and number is:

        # for String ABZ and its corresponding number n:
        # n = (A+1) * 26^2 + (B+1) * 26^1 + (Z+1) * 26^0
        # Why (A+1)? Because in char system 'A' is 0, but in excel system 'A' is 1. Every char get an extra 1.

        # Inorder to get Z, or whatever char is at Z, we will first do a minus 1 on both sides:

        # both sides -1
        # n-1 = (A+1) * 26^2 + (B+1) * 26^1 + Z
        # Then do a %26 we will get Z.

        # (n-1)%26 =  Z                                                  (1)
        # (n-1)/26 = (A+1) * 26^1 + (B+1) * 26^0                         (2)
        # With the above equations, we can understand why we need the n-- at first of every loop:
        # For each loop, we use (1) to obtain what the current char is.
        # And we divide n-1 by 26 to get (2), in preparation for the next loop.
        
        ans = ''
        while columnNumber > 0:
            columnNumber -= 1
            rem = columnNumber % 26
            columnNumber = columnNumber // 26
            ans += chr(ord('A') + rem)
        return ans[::-1]
# Time Complexity: O(log26(N))
# Space Complexity: O(1)

# NOTE:
# https://leetcode.com/problems/excel-sheet-column-title/discuss/441430/Detailed-Explanation-Here's-why-we-need-n-at-first-of-every-loop-(JavaPythonC%2B%2B)
# https://leetcode.com/problems/excel-sheet-column-title/solution/


if __name__ == '__main__':
    sol = Solution()
    print(sol.convertToTitle(1))
    print(sol.convertToTitle(28))
    print(sol.convertToTitle(701))
