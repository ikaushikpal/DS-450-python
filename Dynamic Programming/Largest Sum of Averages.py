from typing import List


class Solution:
    def f(self, nums, row, pos):
        if (row, pos) in self.memo:
            return self.memo[(row, pos)]

        if row == 0:
            self.memo[(row, pos)] = sum(nums[pos:]) / (len(nums) - pos)
            return self.memo[(row, pos)]

        total = avg  = nums[pos]
        count = 1
        maxx = float('-inf')

        for i in range(pos+1, len(nums)-row+1):
            maxx = max(maxx, self.f(nums, row-1, i) + avg)
            total += nums[i]
            count += 1
            avg = total / count
        
        self.memo[(row, pos)] = maxx
        return self.memo[(row, pos)]


    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        self.memo = {}
        return self.f(nums, k-1, 0)

if __name__ == '__main__':
    sol = Solution()
    print(sol.largestSumOfAverages([9,1,2,3,9], 3))
    print(sol.largestSumOfAverages([1,2,3,4,5,6,7], 4))