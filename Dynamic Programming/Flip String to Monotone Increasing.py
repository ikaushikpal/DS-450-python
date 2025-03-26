# A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

# You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

# Return the minimum number of flips to make s monotone increasing.


# Example 1:
# Input: s = "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.


# Example 2:
# Input: s = "010110"
# Output: 2
# Explanation: We flip to get 011111, or alternatively 000111.


# Example 3:
# Input: s = "00011000"
# Output: 2
# Explanation: We flip to get 00000000.


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # this is a dp problem
        # intuition:
        # take 1 length string from left
        # and add new char from left
        
        # if new char is 1 then no problem
        # because string has to be monotonic increasing
        # and also increment oneCounter by 1
        
        # if new char is 0 then two possibilities arrives
        # FIRST: convert 0 to 1, increment countFlips by 1
        # SECOND: convert all previous 1's to 0
        # take the minimum of FIRST, SECOND and store to countFlips
        
        
        countFlips = countOnes = 0
        for digit in s:
            if digit == '1':
                countOnes += 1
            else:
                countFlips = min(countFlips + 1, countOnes)
        return countFlips
# Time Complexity: O(n)
# Space Complexity: O(1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.minFlipsMonoIncr("00110"))
    print(sol.minFlipsMonoIncr("010110"))
    print(sol.minFlipsMonoIncr("00011000"))