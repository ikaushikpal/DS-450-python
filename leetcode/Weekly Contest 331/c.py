from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        if k == 1:
            return min(nums)
        
        prevPrev = nums[0]
        prev = nums[1]
        ppw = pw = 1
        ans = float('inf')

        for i in range(2, len(nums)):
            curr = max(prevPrev, nums[i])
            currw = ppw + 1

            if  currw >= k:
                ans = min(ans, curr)
            
            if ppw < k - 1:
                if pw > ppw:
                    prevPrev = prev
                    ppw = pw
                else:
                    prevPrev = min(prevPrev, prev)
            else:
                prevPrev = min(prevPrev, prev)

            if pw < k - 1:
                if currw > pw:
                    prev = curr
                    pw = currw
                else:
                    prev = min(prev, curr)
            else:
                prev = min(prev, curr)
        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.minCapability([24,1,55,46,4,61,21,52], 3))