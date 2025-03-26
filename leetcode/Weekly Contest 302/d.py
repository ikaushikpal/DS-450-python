from typing import List
from collections import Counter




class Solution:
    def gcd(self, a, b):
        if a == 0:
            return b
        return self.gcd(b % a, a)
 
    def lcm(self, a,b):
        return a * b // self.gcd(a, b)

    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        lcm = numsDivide[0]
        for i in range(1, len(numsDivide)):
            lcm = self.gcd(lcm, numsDivide[i])
        
        c = Counter(nums)
        sortedNums = list(set(nums))
        sortedNums.sort()
        res = 0
        for num in sortedNums:
            if lcm % num == 0:
                return res
            res += c[num]
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.minOperations(nums = [2,3,2,4,3], numsDivide = [9,6,9,3,15]))