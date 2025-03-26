# import bisect


# class Solution:
#     def helper(self, stalls, index, leftIndex, rightIndex, k):
#         if k <= 0:
#             return 0
        
#         if index < 0 or index >= len(stalls):
#             return 0
        
#         if (index, k) in self.memo:
#             return self.memo[(index, k)]

#         ans = 0
#         if leftIndex >= 0:
#             ans = max(ans, self.helper(stalls, leftIndex, leftIndex - 1, rightIndex, k - (stalls[index][0] - stalls[leftIndex][0])))
        
#         if rightIndex < len(stalls):
#             ans = max(ans, self.helper(stalls, rightIndex, leftIndex, rightIndex+ 1, k - (stalls[rightIndex][0] - stalls[index][0])))

#         self.memo[(index, k)] = stalls[index][1] + ans
#         return self.memo[(index, k)]
        
#     def maxFlavoredIceCreams(self, stalls, curpos, k):
#         stalls.sort()
#         temp = [stall[0] for stall in stalls]
        
#         rightPos = bisect.bisect_right(temp, curpos)
#         leftPos = rightPos - 1
#         ans = 0

#         if 0 <= leftPos < len(stalls):
#             self.memo = {}
#             ans = max(ans, self.helper(stalls, leftPos, leftPos - 1, leftPos + 1, k - (curpos - stalls[leftPos][0])))
        
#         if 0 <= rightPos < len(stalls):
#             self.memo = {}
#             ans = max(ans, self.helper(stalls, rightPos, rightPos - 1, rightPos + 1, k - (stalls[rightPos][0] - curpos)))

#         return ans


# print(Solution().maxFlavoredIceCreams([[1, 7], [10, 6], [3, 5], [4, 7]], 6, 8))
# print(Solution().maxFlavoredIceCreams([[1, 3],[4, 2],[2, 1],[5, 10]], 6, 8))

from typing import List


class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a%b)
    
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        i = j = 0
        ans = 0
        
        while j < len(nums):
            if nums[j] < k:
                j += 1
                continue

            currentGcd = nums[j]
            i = j
            t = 0
            
            while currentGcd >= k and j < len(nums):
                currentGcd = self.gcd(currentGcd, nums[j])

                if currentGcd == k:
                    if nums[j] == k:
                        t += j - i + 1
                    else:
                        t += t
                j += 1
            ans += t

        return ans


print(Solution().subarrayGCD(nums = [9,3,1,2,6,3], k = 3))