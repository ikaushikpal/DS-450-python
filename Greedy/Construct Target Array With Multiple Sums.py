# You are given an array target of n integers. From a starting array arr consisting of n 1's, you may perform the following procedure :

# let x be the sum of all elements currently in your array.
# choose index i, such that 0 <= i < n and set the value of arr at index i to x.
# You may repeat this procedure as many times as needed.
# Return true if it is possible to construct the target array from arr, otherwise, return false.

 

# Example 1:
# Input: target = [9,3,5]
# Output: true
# Explanation: Start with arr = [1, 1, 1] 
# [1, 1, 1], sum = 3 choose index 1
# [1, 3, 1], sum = 5 choose index 2
# [1, 3, 5], sum = 9 choose index 0
# [9, 3, 5] Done


# Example 2:
# Input: target = [1,1,1,2]
# Output: false
# Explanation: Impossible to create target array from [1,1,1,1].


# Example 3:
# Input: target = [8,5]
# Output: true
 

from collections import Counter
import heapq
from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        maxEle = max(target)
        N = len(target)
        c = Counter(target)
        arr = [1] * N
        total = N
        
        while total <= maxEle:
            if total in c:
                c[total] -= 1
            
            minEle = heapq.heappop(arr)
            heapq.heappush(arr, total)
            total = 2*total - minEle
        
        for key, value in c.items():
            if key == 1:
                continue
            
            if value > 0:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPossible([9,3,5]))
    print(sol.isPossible([1,1,1,2]))
    print(sol.isPossible([8,5]))