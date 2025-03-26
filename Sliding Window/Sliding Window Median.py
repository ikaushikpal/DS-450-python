import heapq
from typing import List


class MedianFinder:
    def __init__(self):
        self.min_heap = [] # right section
        self.max_heap = [] # left section

    def balanceHeaps(self) -> None:
        #Balance the two heaps size , such that difference is not more than one.
        if abs(len(self.min_heap) - len(self.max_heap)) <= 1:
            return # if difference is of 0 or 1 then do nothing
        
        if len(self.min_heap) > len(self.max_heap):
            popped_ele = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -popped_ele)
        
        else:
            popped_ele = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -popped_ele)
        

    def findMedian(self) -> float:
        # return the median of the data received till now.
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        
        elif len(self.min_heap) < len(self.max_heap):
            return -self.max_heap[0]
        
        else:
            return (self.min_heap[0] + (-self.max_heap[0]))/2

    
    def addNum(self, x:int ) -> None:
        #:param x: value to be inserted
        #:return: None
        if len(self.min_heap) == 0: # initial when heap is empty
            heapq.heappush(self.min_heap, x)

        elif self.min_heap[0] < x:
            heapq.heappush(self.min_heap, x)

        else:
            heapq.heappush(self.max_heap, -x)

        self.balanceHeaps()
    
    def pop(self):
        # delete the median element
        if len(self.min_heap) > len(self.max_heap):
            ans = heapq.heappop(self.min_heap)
        else:
            ans = -heapq.heappop(self.max_heap)
        self.balanceHeaps()
        return ans
    
    def remove(self, num):
        temp = []
        while True:
            popedEle = self.pop()
            if popedEle == num:
                break
            temp.append(popedEle)
        
        for ele in temp:
            self.addNum(ele)

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        mf = MedianFinder()
        for num in nums[:k]:
            mf.addNum(num)
        ans = [mf.findMedian()]
        for i in range(min(k, len(nums)), len(nums), 1):
            mf.remove(nums[i - k])
            mf.addNum(nums[i])
            ans.append(mf.findMedian())
        return ans


sol = Solution()
print(sol.medianSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))