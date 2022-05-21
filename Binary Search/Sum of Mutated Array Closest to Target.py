# Given an integer array arr and a target value target, return the integer value such that when we change all the integers larger than value in the given array to be equal to value, the sum of the array gets as close as possible (in absolute difference) to target.

# In case of a tie, return the minimum such integer.

# Notice that the answer is not neccesarilly a number from arr.

 

# Example 1:
# Input: arr = [4,9,3], target = 10
# Output: 3
# Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.



# Example 2:
# Input: arr = [2,3,5], target = 10
# Output: 5



# Example 3:
# Input: arr = [60864,25176,27249,21296,20204], target = 56803
# Output: 11361


from typing import List


class Solution:
    def calcDiff(self, arr, mid):
        total = 0
        for val in arr:
            if val < mid:
                total += val
            else:
                total += mid
        return total
    
    def findBestValue(self, arr: List[int], target: int) -> int:
        low, high = 0, max(arr)
        minDiff, res = float('inf'), float('inf')
        
        while low <= high:
            mid = (low + high) // 2
            diff = target - self.calcDiff(arr, mid)
            
            if abs(diff) < minDiff:
                minDiff = abs(diff)
                res = mid
            
            if abs(diff) == minDiff:
                res = min(res, mid)
            
            if diff > 0:
                low = mid + 1
            else:
                high = mid - 1
        
        return res
        


if __name__ == '__main__':
    sol = Solution()
    print(sol.findBestValue([4,9,3], 10))
    print(sol.findBestValue([2,3,5], 10))
    print(sol.findBestValue([60864,25176,27249,21296,20204], 56803))