from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        seen = set(banned)
        tot = ans = 0
        for i in range(1, n+1):
            if i not in seen:
                tot += i
                if tot <= maxSum:
                    ans += 1
                else:
                    break
        return ans