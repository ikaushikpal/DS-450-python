import heapq
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return (nums[0] + k) % 1_000_000_007
        
        minHeap = nums
        heapq.heapify(minHeap)
        
        while k > 0:
            val = heapq.heappop(minHeap)
            nextMin = heapq.heappop(minHeap)
            need = min(max(nextMin - val, 1), k)
            
            heapq.heappush(minHeap, val+need)
            heapq.heappush(minHeap, nextMin)
            k -= need

        ans = 1
        for _ in range(len(minHeap)):
            ans *= heapq.heappop(minHeap)
        
        return ans % 1_000_000_007


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumProduct([0,4], 5))