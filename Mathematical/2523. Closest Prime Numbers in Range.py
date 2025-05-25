# Given two positive integers left and right, find the two integers num1 and num2 such that:

# left <= num1 < num2 <= right .
# Both num1 and num2 are prime numbers.
# num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
# Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

 
# Example 1:
# Input: left = 10, right = 19
# Output: [11,13]
# Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
# The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
# Since 11 is smaller than 17, we return the first pair.

# Example 2:
# Input: left = 4, right = 6
# Output: [-1,-1]
# Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
 

# Constraints:
# 1 <= left <= right <= 10^6


from typing import List


class Solution:
    def sieve(self, N):
        arr = [True] * (N + 1)
        arr[0] = arr[1] = False

        i = 2
        while i * i <= N:
            if arr[i]:
                for j in range(i*i, N + 1, i):
                    arr[j] = False
            i += 1

        return arr

    def closestPrimes(self, left: int, right: int) -> List[int]:
        arr = self.sieve(right)
        primes = []

        for i in range(left, right +1):
            if arr[i]:
                primes.append(i)
                
        ans = [-1, -1]
        min_gap = float('inf')

        for i in range(1, len(primes)):
            gap = primes[i] - primes[i - 1]

            if gap < min_gap:
                min_gap = gap
                ans = primes[i-1 : i + 1]
        return ans
# Time Complexity: O(Rlog(logR))
# Space Complexity: O(R)


if __name__ == '__main__':
    sol = Solution()
    print(sol.closestPrimes(left = 10, right = 19))
    print(sol.closestPrimes(left = 4, right = 6))