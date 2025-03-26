# Given an integer n, return the number of prime numbers that are strictly less than n.

# Example 1:
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# Example 2:
# Input: n = 0
# Output: 0

# Example 3:
# Input: n = 1
# Output: 0


import math


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # Sieve Of Eratosthenes
        primes = [1] * n 
        primes[0] = primes[1] = 0

        for i in range(2, math.ceil(math.sqrt(n))):
            if primes[i]:
                primes[i * i : n : i] = [0] * len(primes[i *  i : n : i])

        return sum(primes)

# for crazy fast solution

# from math import sqrt, ceil
# from numpy import ones, sum


# class Solution:
#     def countPrimes(self, n: int) -> int:
#         if n <= 2:
#             return 0
        
#         # Sieve Of Eratosthenes
#         primes = ones(n, dtype=bool)
#         primes[0] = primes[1] = False

#         for i in range(2, ceil(sqrt(n))):
#             if primes[i]:
#                 primes[i * i : n : i] = False

#         return sum(primes)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countPrimes(100_000_000))
    print(sol.countPrimes(4))
    print(sol.countPrimes(1))
    print(sol.countPrimes(0))