# Given two binary strings A and B consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.
# Note: The input strings may contain leading zeros but the output string should not have any leading zeros.


# Example 1:
# Input:
# A = "1101", B = "111"
# Output: 10100
# Explanation:
#  1101
# + 111
# 10100


# Example 2:
# Input: 
# A = "10", B = "01"
# Output: 11
# Explanation: 
#   10
# + 01
#   11


class Solution:
    def addBinary(self, A, B):
        A = A.lstrip('0')
        B = B.lstrip('0')
        i, j = len(A) - 1, len(B) - 1
        ans = ''
        carryBit = 0

        while i >= 0 and j >= 0:
            bitA = int(A[i])
            bitB = int(B[j])

            sumBit = bitA ^ bitB ^ carryBit
            carryBit = (bitA & carryBit) | (bitB & carryBit) | (bitA & bitB)

            ans += str(sumBit)
            i -= 1
            j -= 1

        while i >= 0:
            bitA = int(A[i])

            sumBit = bitA ^ carryBit
            carryBit = bitA & carryBit

            ans += str(sumBit)
            i -= 1

        while j >= 0:
            bitB = int(B[j])

            sumBit = bitB ^ carryBit
            carryBit = bitB & carryBit

            ans += str(sumBit)
            j -= 1

        if carryBit:
            ans += str(carryBit)

        return ans[::-1]
# Time Complexity: O(max(len(A), len(B)))
# Space Complexity: O(max(len(A), len(B)))


if __name__ == '__main__':
    sol = Solution()
    print(sol.addBinary("1101", "111"))
    print(sol.addBinary("10", "01"))