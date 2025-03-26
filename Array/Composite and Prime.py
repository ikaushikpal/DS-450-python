# Given two integers L and R find the difference of number of composites and primes between the range L and R (both inclusive).

# Example 1:
# Input: L = 4, R = 6
# Output: 1
# Explanation: Composite no. are 4 and 6.
# And prime is 5.

# Example 2:
# Input: L = 4, R = 4
# Output: 1
# Explanation: There is no prime no. in [L,R]


from math import sqrt, ceil


class Solution:
    def sieveOfEratosthenes(self, n):
        sieve = [True] * n
        sieve[0] = sieve[1] = False
        
        for i in range(2,ceil(sqrt(n))):
            if sieve[i]:
                for j in range(i*i, n, i):
                    sieve[j] = False
        
        primes = []
        for i in range(n):
            if sieve[i]:
                primes.append(i)
        return primes
        
    def Count(self, L, R):
        limit = ceil(sqrt(R))
        primes = self.sieveOfEratosthenes(limit + 1)
        isPrime = [True] * (R-L+1)

        for i in primes:
            start = max(ceil(L / i) * i, i*i)
            end = R + 1
            step = i
            for j in range(start, end, step):
                isPrime[j - L] = False

        totalPrimes = totalComposites = 0
        for i in range(len(isPrime)):
            if i + L == 1:
                continue
            
            if isPrime[i]:
                totalPrimes += 1
            else:
                totalComposites += 1
        
        return totalComposites - totalPrimes


if __name__ == '__main__':
    sol = Solution()
    print(sol.Count(1, 24))