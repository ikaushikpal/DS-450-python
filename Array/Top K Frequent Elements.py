# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]


from collections import Counter
import heapq
from itertools import chain
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solution 1:
        # one liner
        ######
        # return [x[0] for x in Counter(nums).most_common()[:k]]
        
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        # SOlution 2:
        ######
        # counts = Counter(nums)
        # lst = counts.most_common(k)
        # return list(zip(*lst))[0]
        
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        # Solution 3:
        ######
        # c = Counter(nums)
        # minHeap = [(value, key) for key, value in c.items()]
        # heapq.heapify(minHeap)
        
        # while len(minHeap) > k:
        #     heapq.heappop(minHeap)
        
        # ans = [ele[1] for ele in minHeap]
        # return ans[::-1]

        # Time Complexity: O(nlogn)
        # Space Complexity: O(n)


        # Solution 4:
        ######
        bucket = [[] for _ in range(len(nums) + 1)]
        c = Counter(nums)

        for num, freq in c.items():
            bucket[freq].append(num)
             
        flat_list = list(chain(*bucket))
        return flat_list[::-1][:k]
        # Time Complexity: O(n)
        # Space Complexity: O(n)


if __name__ == '__main__':
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3], 2))