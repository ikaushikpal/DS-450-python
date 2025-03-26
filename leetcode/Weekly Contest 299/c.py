from typing import List


class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        nums3 = [val2-val1 for val1, val2 in zip(nums1, nums2)]
        total1 = sum(nums1)
        total2 = sum(nums2)
        score = max(total1, total2)
        add, i, j = self.maxSubArraySum(nums3, len(nums3))
        score = max(score, total1 + add)
        return score

    def maxSubArraySum(self, arr, size):
        currentBest, overallBest = 0, -10e7
        start = end = 0
        finalStart, finalEnd = 0, 0

        for i, val in enumerate(arr):
            if val + currentBest >= val:
                currentBest += val
            else:
                currentBest = val
                start = i
            end = i
            if currentBest > overallBest:
                overallBest = currentBest
                finalStart = start
                finalEnd = i
        
        return (overallBest, finalStart, finalEnd)


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumsSplicedArray(nums1 = [60,60,60], nums2 = [10,90,10]))
    print(sol.maximumsSplicedArray(nums1 = [20,40,20,70,30], nums2 = [50,20,50,40,20]))
    print(sol.maximumsSplicedArray(nums1 = [7,11,13], nums2 = [1,1,1]))