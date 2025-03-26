from typing import List

# this problem is very similar to minimum allocation books[GOOGLE]
# split array largest sum

class Solution:
    def isValid(self, weights, days, maxSum):
        total = 0

        for num in weights:
            total += num
            # if total exceeds maxSum
            # that means we need to split array here
            if total > maxSum:
                days -= 1
                total = num
            
            # if we splitted array more than its allowed then
            # simply return False meaning we can not form split
            if days <= 0:
                return False

        # we can split array in to m parts
        return True
    
    def findMaxSum(self, weights):
        total, maxValue = 0, float('-inf')
        for num in weights:
            total += num
            maxValue = max(maxValue, num)
        
        return (maxValue, total)

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # edge case
        if days > len(weights):
            return -1
        
        maxValue, total = self.findMaxSum(weights)

        if days == len(weights):
            return maxValue

        if days == 1:
            return total

        low, high = maxValue, total
        ans = -1

        while low <= high:
            mid = (low + high) >> 1

            # if we can split array into m parts
            # with mid as maxSum then go left for more minimum ans
            if self.isValid(weights, days, mid):
                ans = mid
                high = mid - 1
            else:
                # could not split into m with current mid, go right
                low = mid + 1
        
        return ans