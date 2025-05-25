# Given two numbers L and R(L<R). Count all the prime numbers in the range [L, R].

# Example 1:
# Input:
# L=1,R=10
# Output:
# 4
# Explanation:
# There are 4 primes in this range, 
# which are 2,3,5 and 7.

# Example 2:
# Input:
# L=5,R=10
# Output:
# 2
# Explanation:
# There are 2 primes in this range, 
# which are 5 and 7.

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function countPrimes() which takes the two integers L and R as input parameters and returns the number of prime numbers in the range [L, R].

# Expected Time Complexity:O(RLogLog(R))
# Expected Auxillary Space:O(R)

# Constraints:
# 1<=L<R<=2*10^5


class Solution:
    def countPrimes(self,L,R):
        sieve = [True] * (R + 1)
        sieve[0] = sieve[1] = False
        
        i = 2
        while i * i <= R:
            if sieve[i]:
                for j in range(i*i, R + 1, i):
                    sieve[j] = False
            i += 1
        
        prefix_count = [0] * (R + 1)
        for i in range(2, R +1):
            prefix_count[i] = prefix_count[i - 1]
            
            if sieve[i]:
                prefix_count[i] += 1
        
        return prefix_count[R] - prefix_count[L - 1]
# Time Complexity:O(RLogLog(R))
# Space Space:O(R)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countPrimes(L=1,R=10))
    print(sol.countPrimes(L=5,R=10))