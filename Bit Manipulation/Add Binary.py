# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"


# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # making leading zeros
        maxLength = max(len(a), len(b))
        a = f'{a:0>{maxLength}}'[::-1]
        b = f'{b:0>{maxLength}}'[::-1]

        # initialization
        # sum = a ^ b ^ cin
        # carry = (a & b) | ((a ^ b) & cin)
        carryBit = 0
        ans = ''
        
        for i in range(maxLength):
            aXorB = int(a[i]) ^ int(b[i])
            aAndB = int(a[i]) & int(b[i])
            sumBit = aXorB ^ carryBit
            carryBit = aAndB | (aXorB & carryBit)
            ans += str(sumBit)
        
        if carryBit:
            ans += '1'
        
        return ans[::-1]
# Time Complexity: O(N)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.addBinary('11', '1'))
    print(sol.addBinary('1010', '1011'))