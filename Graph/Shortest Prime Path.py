# You are given two four digit prime numbers Num1 and Num2. Find the distance of the shortest path from Num1 to Num2 that can be attained by altering only one single digit at a time. Every number obtained after changing a digit should be a four digit prime number with no leading zeros.


# Example 1:
# Input:
# Num1 = 1033 
# Num2 = 8179
# Output: 6
# Explanation:
# 1033 -> 1733 -> 3733 -> 3739 -> 3779
#                  -> 8779 -> 8179.
# There are only 6 steps required to reach
# Num2 from Num1, and all the intermediate
# numbers are 4 digit prime numbers.


# Example 2:
# Input:
# Num1 = 1033 
# Num2 = 1033
# Output:


from math import ceil, sqrt
from collections import deque


class Prime:
    primes = None
    
    def __init__(self):
        if Prime.primes:
            return
        
        self.sieve()
        
    def sieve(self, N = 10000): 
        Prime.primes = [True] * N
        
        for num in range(2, round(ceil(sqrt(N))) + 1):
            if not Prime.primes[num]:
                continue
            
            for i in range(num*num, N, num):
                Prime.primes[i] = False
     
    def checkPrime(self, num):
        return self.primes[num]
        
class Solution:
    def __init__(self):
        # Every index of prime stores zero or one
        # If prime[i] is zero means i is not a prime
        # If prime[i] is one means i is a prime
        self.prime = Prime()

    def shortestPath(self, base, target):   
        base = str(base)
        target = str(target)
        
        queue = deque()
        seen = set()
        
        queue.append((base, 0))
        seen.add(base)
        
        while queue:
            num, moves = queue.popleft()
            if num == target:
                return moves

            for i in range(4):
                for j in range(10):
                    newNum = num[:i] + str(j) + num[i+1:]

                    if newNum == num:
                        continue
                    
                    if int(newNum) < 1000:
                        continue
                    
                    if newNum in seen:
                        continue
                    
                    if self.prime.checkPrime(int(newNum)):
                        queue.append((newNum, 1 + moves))
                        seen.add(newNum)
        return -1
# Time Complexity: O(NlogN)
# Space Space: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.shortestPath(1033, 8179))
    print(sol.shortestPath(1033, 1033))