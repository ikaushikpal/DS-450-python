# Given a number N. Find its unique prime factors in increasing order.

# Example 1:
# Input: N = 100
# Output: 2 5
# Explanation: 2 and 5 are the unique prime
# factors of 100.

# Example 2:
# Input: N = 35
# Output: 5 7
# Explanation: 5 and 7 are the unique prime
# factors of 35.
 

# Your Task:
# You don't need to read or print anything. Your task is to complete the function AllPrimeFactors() which takes N as input parameter and returns a list of all unique prime factors of N in increasing order.

# Expected Time Complexity: O(N)
# Expected Space Complexity: O(N)
 
# Constraints:
# 1 <= N  <= 10^6


from math import sqrt

class Solution:
    def AllPrimeFactors(self, N):
        factors = []
        i = 2 # starting from smallest valid prime
        
        # using <= if N is prefect square
        # optimization N  -> sqrt(N)
        while i <= sqrt(N):
            # if i is a factor of N
            if N % i == 0:
                factors.append(i)
                
                # reducing N, so next time multiple of i can not divide it 
                # by doing this we are not checking if i is prime or not
                while N % i == 0:
                    N = N // i
            i += 1
        
        # lets say N is prime itself then need to add N 
        # 1 is not prime thats why not adding it
        if N > 1:
            factors.append(N)
        return factors
# Time Complexity: O(sqrt(N))
# Space Complexity: O(sqrt(N))


if __name__ == '__main__':
    sol = Solution()
    print(sol.AllPrimeFactors(100))
    print(sol.AllPrimeFactors(35))