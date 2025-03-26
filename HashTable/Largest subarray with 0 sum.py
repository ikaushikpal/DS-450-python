from typing import List

class Solution:
    def maxLen(self, n:int, arr:List[int]) -> int:
        maxLength = 0

        ht = {0:-1} # current_sum : index
        current_sum = 0
        for i in range(n):
            current_sum += arr[i]

            if current_sum not in ht:
                ht[current_sum] = i
            else:
                windowLength = i - ht[current_sum]
                maxLength = max(maxLength, windowLength)

        return maxLength