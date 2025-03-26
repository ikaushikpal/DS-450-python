from typing import List
from math import floor, sqrt
import heapq


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] = -gifts[i]
        heapq.heapify(gifts)

        ans = 0
        for i in range(k):
            x = -heapq.heappop(gifts)
            x = floor(sqrt(x))
            heapq.heappush(gifts, -x)
        
        return sum(gifts) * -1
        

sol = Solution()
print(sol.pickGifts([25,64,9,4,100], 4))