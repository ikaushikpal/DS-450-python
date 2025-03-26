# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
 

# Example 1:

# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]

# Example 2:

# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]


import bisect
from collections import deque
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def calcDist(x1, x2):
            return abs(x1 - x2)

        N = len(arr)
        k = min(k, N)
        index = bisect.bisect_left(arr, x) - 1
        i, j = index, (index + 1) % N
        ans = deque()

        while len(ans) < k:
            iDist = calcDist(arr[i], x)
            jDist = calcDist(arr[j], x)

            if iDist < jDist:
                ans.appendleft(arr[i])
                i = (i - 1 + N) % N

            elif iDist > jDist:
                ans.append(arr[j])
                j = (j + 1) % N

            elif arr[i] <= arr[j]:
                ans.appendleft(arr[i])
                i = (i - 1 + N) % N
                
            else:
                ans.append(arr[j])
                j = (j + 1) % N
        return ans
# TC = O(min(K, N))
# SC = O(min(K, N))


if __name__ == '__main__':
    sol = Solution()
    print(sol.findClosestElements([1,2,3,4,5], 4, 3))