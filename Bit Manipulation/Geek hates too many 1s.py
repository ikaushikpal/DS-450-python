# Given an non-negative integer n. You are only allowed to make set bit unset. You have to find the maximum possible value of query so that after performing the given operations, no three consecutive bits of the integer query are set-bits. 



# Example 1:
# Input:
# n = 2
# Output: 
# 2
# Explanation: 
# 2's binary form is 10, no 3 consecutive set bits are here. 
# So, 2 itself would be answer


# Example 2:
# Input:
# n = 7
# Output: 
# 6
# Explanation: 
# 7's binary form is .....00111.We can observe that 3
# consecutive bits are set bits. This is not allowed.
# So, we can perform the operation of changing set 
# bit to unset bit. Now, the number 
# becomes 6 that is .....00110. It satisfies the 
# given condition. Hence, the maximum possible 
# value is 6.


from math import log, floor


class Solution:
    def countBits(self, n):
        return int(floor(log(n, 2)))
        
    def noConseBits(self, n : int) -> int:
        if n == 0:
            return 0
            
        ans = consecutiveBits = 0
        length = self.countBits(n)

        for i in range(length, -1, -1):
            mask = 1 << i
            bit = 1 if n & mask else 0
            ans = ans << 1

            if bit:
                consecutiveBits += 1
            else:
                consecutiveBits = 0
                
            if consecutiveBits < 3:
                ans += bit
            else:
                consecutiveBits = 0
        return ans
# Time Complexity: O(log n)
# Space Complexity: O(1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.noConseBits(2))