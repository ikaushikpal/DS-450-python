# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


# Example 1:
# Input: x = 2.00000, n = 10
# Output: 1024.00000


# Example 2:
# Input: x = 2.10000, n = 3
# Output: 9.26100


# Example 3:
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25


class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n < 0:
            x = 1 / x
            n = -n

        while n:
            if n & 1:
                res = res * x
                n -= 1
                
            n = n >> 1
            x = x * x
        
        return res
# Time Complexity: O(log(n))
# Space Complexity: O(1)
    

if __name__ == '__main__':
    sol = Solution()
    print(sol.myPow(x = 2.00000, n = 10))
    print(sol.myPow(x = 2.10000, n = 3))
    print(sol.myPow(x = 2.00000, n = -2))