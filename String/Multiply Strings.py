# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"


# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        res = []
        carry = 0

        for i, char1 in enumerate(num1[::-1]):
            k = i
            carry = 0
            for j, char2 in enumerate(num2[::-1]):
                val = int(char2) * int(char1) + carry
                
                if k < len(res):
                    val += int(res[k])
                    res[k] = str(val % 10)
                else:
                    res.append(str(val % 10))

                carry = val // 10
                k += 1

            if carry > 0:
                res.append(str(carry))

        return ''.join(res[::-1])
# Time Complexity: O(n^2)
# Space Complexity: O(n)


if __name__ == '__main__':
    print(Solution().multiply('2', '3'))
    print(Solution().multiply('123', '456'))
    print(Solution().multiply('123456789', '987654321'))
    print(Solution().multiply('0', '0'))
    print(Solution().multiply('9133', '0'))