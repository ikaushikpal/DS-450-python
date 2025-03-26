from typing import List
from collections import Counter


class Solution:
    def findMaxTwo(self, arr):
        first = second = float('-inf')
        
        for i in range(len(arr)):
            if arr[i] > first:
                second = first
                first = arr[i]

            elif arr[i] > second:
                second = arr[i]

        return first, second

    def findDigitSum(self, num):
        res = 0
        while num > 0:
            res += num % 10
            num //= 10
        return res

    def maximumSum(self, nums: List[int]) -> int:
        digitsSum = [self.findDigitSum(num) for num in nums]
        bucket = {}
        for i, ds in enumerate(digitsSum):
            if ds not in bucket:
                bucket[ds] = [nums[i]]
            else:
                bucket[ds].append(nums[i])
        maxSum = -1
        for ds, arr in bucket.items():
            if len(arr) > 1:
                first, second = self.findMaxTwo(arr)
                maxSum = max(maxSum, first + second)
        return maxSum


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumSum([4,6,10,6]))