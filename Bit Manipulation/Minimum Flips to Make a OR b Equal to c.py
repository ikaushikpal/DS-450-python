# Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
# Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

 
# Example 1:
# Input: a = 2, b = 6, c = 5
# Output: 3
# Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)


# Example 2:
# Input: a = 4, b = 2, c = 7
# Output: 1


# Example 3:
# Input: a = 1, b = 2, c = 3
# Output: 0


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        
        while a or b or c:
            aLastBit = a & 1
            bLastBit = b & 1
            cLastBit = c & 1
            
            if cLastBit == 0:
                ans += aLastBit + bLastBit
            elif aLastBit | bLastBit == 0:
                ans += 1
                
            a = a >> 1
            b = b >> 1
            c = c >> 1
        return ans
# Time Complexity: O(log(max(a, b, c)))
# Space Complexity: O(1)



if __name__ == '__main__':
    sol = Solution()
    print(sol.minFlips(2, 6, 5))
    print(sol.minFlips(4, 2, 7))
    print(sol.minFlips(1, 2, 3))