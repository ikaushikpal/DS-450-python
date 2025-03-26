from collections import Counter
from typing import List


class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        t = len(nums) - sum(1 for i in c.values() if i == 1)
        ans = k+ t

        maxWindAllowed = ans // k
        newCost = 0
        window = set()
        start = i = 0
        while maxWindAllowed > 1 and i < len(nums):
            if nums[i] in window:
                maxWindAllowed -= 1
                window = set([nums[i]])
                newCost += k
                start = i
            else:
                window.add(nums[i])
            i += 1
        
        c = Counter(nums[start : ])
        t = len(nums[start:]) - sum(1 for i in c.values() if i == 1)
        newCost += t + k

        return min(ans, newCost)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minCost([1,2,1,2,1,3,3], 2))