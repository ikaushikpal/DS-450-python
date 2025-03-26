# You are given an integer array of unique positive integers nums. Consider the following graph:

# There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
# There is an undirected edge between nums[i] and nums[j] if nums[i] and nums[j] share a common factor greater than 1.
# Return the size of the largest connected component in the graph.

 

# Example 1:
# Input: nums = [4,6,15,35]
# Output: 4


# Example 2:
# Input: nums = [20,50,9,63]
# Output: 2


# Example 3:
# Input: nums = [2,3,6,7,4,12,21,39]
# Output: 8


from collections import defaultdict
from typing import List


class Disjoint:
    def __init__(self, n=0):
        self.n = n
        self.array = [-1] * self.n

    def add(self):
        self.array.append(-1)
        self.n += 1

    def find(self, n):
        if self.array[n] < 0:
            return (n,  -self.array[n])
        result = self.find(self.array[n])
        self.array[n] = result[0]
        return result
    
    def union(self, set1, set2):
        parent_of_set1, rank_of_set1 = self.find(set1)
        parent_of_set2, rank_of_set2 = self.find(set2)

        if parent_of_set1 == parent_of_set2:
            return False

        if rank_of_set1 > rank_of_set2:
            self.array[parent_of_set1] += self.array[parent_of_set2]
            self.array[parent_of_set2] = parent_of_set1
            
        else:
            self.array[parent_of_set2] += self.array[parent_of_set1]
            self.array[parent_of_set1] = parent_of_set2
        return True


class Solution:
    def findPrims(self, n:int)->None:
        arr = [False] * (n+1)
        primes = []

        for i in range(2, n+1, 1):
            if arr[i] == False: # if it not a prime multiple or not marked yet
                arr[i*i:n+1:i] = [True] * len(arr[i*i:n+1:i])
        
        for i in range(2, n+1, 1):
            if arr[i] == 0:
                primes.append(i)
        
        return primes

    def largestComponentSize(self, nums: List[int]) -> int:
        MAX_SIZE = max(nums) + 1
        d = Disjoint(MAX_SIZE)
        factorNumberMap = defaultdict(list)
        allPrimes = self.findPrims(MAX_SIZE)

        for num in nums:
            for prime in allPrimes:
                if num % prime == 0:
                    factorNumberMap[prime].append(num)

        for prime, nums in factorNumberMap.items():
            for i in range(1, len(nums)):
                d.union(nums[i-1], nums[i])

        return -min(d.array)


if __name__ == '__main__':
    s = Solution()
    print(s.largestComponentSize([4,6,15,35]))
    print(s.largestComponentSize([20,50,9,63]))
    print(s.largestComponentSize([2,3,6,7,4,12,21,39]))