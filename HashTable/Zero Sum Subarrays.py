from typing import List
from collections import defaultdict


class Solution:

    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self, arr:List[int], n:int) -> int:
        countSubArrays = 0
        
        ht = defaultdict(lambda : 0) # current_sum : frequency
        ht[0] = 1

        current_sum = 0

        for i in range(n):
            current_sum += arr[i]

            countSubArrays += ht[current_sum]
            ht[current_sum] += 1

        return countSubArrays


if __name__ == '__main__':
    print(Solution().findSubArrays([0,0,5,5,0,0], 6))