from typing import List
from functools import lru_cache

class Solution:
    @lru_cache(None)
    def f(self, cookies, i, partition):
        if i == len(cookies):
            return max(partition)

        # if i in self.memo:
            # return self.memo[i]

        minValue = float('inf')
        for k in range(len(partition)):
            partition[k] += cookies[i]
            minValue = min(minValue, self.f(cookies, i+1, partition))
            partition[k] -= cookies[i]

        # self.memo[i] = minValue
        return minValue

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # self.memo = {}
        return self.f(cookies, 0, [0]*k)


if __name__ == '__main__':
    sol = Solution()
    print(sol.distributeCookies(cookies = [8,15,10,20,8], k = 2))
    print(sol.distributeCookies(cookies = [6,1,3,2,2,4,1,2], k = 3))
    print(sol.distributeCookies([76265,7826,16834,63341,68901,58882,50651,75609],
8))