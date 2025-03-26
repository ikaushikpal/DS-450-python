# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"


# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I


# Example 3:
# Input: s = "A", numRows = 1
# Output: "A"


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        store = [[] for _ in range(numRows)]
        i = 0
        while i < len(s):
            # going down
            row = 0
            while i < len(s) and row < numRows:
                store[row].append(s[i])
                row += 1
                i += 1
            
            # going obliquely up
            row = numRows - 2
            while i < len(s) and row > 0:
                store[row].append(s[i])
                row -= 1
                i += 1
        
        ans = ''
        for level in store:
            ans += ''.join(level)
        return ans
# Time Complexity: O(N)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.convert("PAYPALISHIRING", 3))
    print(sol.convert("PAYPALISHIRING", 4))
    print(sol.convert("A", 1))