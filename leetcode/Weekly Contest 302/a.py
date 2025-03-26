from typing import List
from collections import Counter


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        countPair = remaining = 0
        for freq in c.values():
            if freq & 1:
                remaining += 1
            countPair += (freq >> 1)
        return (countPair, remaining)