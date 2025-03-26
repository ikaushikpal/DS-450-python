from math import ceil, sqrt


class Solution:
    def sieveOfEratosthenes(self, n):
        sieve = [True] * n 
        sieve[0] = sieve[1] = False

        for i in range(2, ceil(sqrt(n))):
            if sieve[i]:
                sieve[i * i : n : i] = [False] * len(sieve[i *  i : n : i])
        
        return sieve

    def primeProduct(self, L, R):
        MOD = 1000000007
        primes = [True] * (R-L+1)
        sieve = self.sieveOfEratosthenes(ceil(sqrt(R+1)))

        # marking non primes from L - R
        for i in range(len(sieve)):
            if sieve[i]:
                start = max(ceil(L / i) * i, i*i)
                primes[start - L :  R+1 : i] = [False] * len(primes[start - L :  R+1 : i])
            
        prod = 1
        for i in range(len(primes)):
            if primes[i]:
                prod *= (i + L)
        
        return prod % MOD


if __name__ == '__main__':
    sol = Solution()
    print(sol.primeProduct(1, 10))
    print(sol.primeProduct(22, 51))