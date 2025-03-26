# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

# Example 1:
# Input: piles = [3,6,7,11], h = 8
# Output: 4

# Example 2:
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30

# Example 3:
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23


from math import ceil
from typing import List


class Solution:
    def isValid(self, piles, hoursRemaining, eatingSpeed):
        for pile in piles:
            hoursRemaining -= int(ceil(pile / eatingSpeed))
            if hoursRemaining < 0:
                return False
        return True
    
    def minEatingSpeed(self, piles: List[int], hoursRemaining: int) -> int:
        piles.sort()
        low, high = 1, max(piles)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if self.isValid(piles, hoursRemaining, mid):
                ans = mid
                high = mid - 1   
            else:
                low = mid + 1
        
        return ans


if __name__== '__main__':
    s = Solution()
    print(s.minEatingSpeed([3,6,7,11], 8))
    print(s.minEatingSpeed([30,11,23,4,20], 5))
    print(s.minEatingSpeed([30,11,23,4,20], 6))