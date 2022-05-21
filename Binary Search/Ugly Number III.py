# An ugly number is a positive integer that is divisible by a, b, or c.

# Given four integers n, a, b, and c, return the nth ugly number.

 

# Example 1:

# Input: n = 3, a = 2, b = 3, c = 5
# Output: 4
# Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
# Example 2:

# Input: n = 4, a = 2, b = 3, c = 4
# Output: 6
# Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.
# Example 3:

# Input: n = 5, a = 2, b = 11, c = 13
# Output: 10
# Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.



class Solution:
    def gcd(self, a,b):
        if a == 0:
            return b
        return self.gcd(b % a, a)
 
    def lcm(self, a, b):
        return a * b // self.gcd(a,b)
    
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        lcm_ab = self.lcm(a, b)
        lcm_bc = self.lcm(b, c)
        lcm_ac = self.lcm(a, c)
        lcm_abc = self.lcm(lcm_ab, c)
        
        low = min(a,b,c)
        high = low * n
        
        while low <= high:
            mid = (low + high) // 2
            term = ((mid//a + mid//b + mid//c) - 
                    (mid//lcm_ab + mid//lcm_bc + mid//lcm_ac) + 
                    (mid//lcm_abc))
            
            if term < n:
                low = mid + 1
            else:
                high = mid - 1
                
        return low


if __name__ == '__main__':
    s = Solution()
    print(s.nthUglyNumber(n = 4, a = 2, b = 3, c = 4))