# You are given two integers L and R, your task is to find the XOR of elements of the range [L, R].

# Example:

# Input: 
# L = 4, R = 8 
# Output:
# 8 
# Explanation:
# 4 ^ 5 ^ 6 ^ 7 ^ 8 = 8

# Your Task:
# Your task is to complete the function findXOR() which takes two integers l and r and returns the XOR of numbers from l to r.

# Expected Time Complexity: O(1).
# Expected Auxiliary Space: O(1).

# Constraints:
# 1<=l<=r<=10^9


class Solution:
    def findXORUtil(self, n):
        # will calculate xor from 1 to n
        # from pattern we can derive

        if n % 4 == 1:
            return 1
        
        if n % 4 == 2:
            return n + 1
        
        if n % 4 == 3:
            return 0
        
        if n % 4 == 0:
            return n

    def findXOR(self, l, r):
        return self.findXORUtil(r) ^ self.findXORUtil(l - 1)
# Time Complexity: O(1)
# Space Complexity: O(1)



if __name__ == '__main__':
    sol = Solution()
    print(sol.findXOR(4, 8))