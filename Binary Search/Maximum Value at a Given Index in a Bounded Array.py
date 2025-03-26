# You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:

# nums.length == n
# nums[i] is a positive integer where 0 <= i < n.
# abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
# The sum of all the elements of nums does not exceed maxSum.
# nums[index] is maximized.
# Return nums[index] of the constructed array.

# Note that abs(x) equals x if x >= 0, and -x otherwise.


# Example 1:
# Input: n = 4, index = 2,  maxSum = 6
# Output: 2
# Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
# There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].


# Example 2:
# Input: n = 6, index = 1,  maxSum = 10
# Output: 3


class Solution:
    def calcNumsSum(self, n, index, num):
        # actual sequence:
        # 1, 2,,, num - 1, num, num - 1, num - 2,,, 1
        # sum(1, 2,,, num - 1, num) = maxPartSum
        maxPartSum = num * (num - 1) // 2

        # leftPartNotInc: the number of elements in the left part of the sequence that are not included in the sum
        # rightPartNotInc: the number of elements in the right part of the sequence that are not included in the sum
        # 1, 2,,, num - 1, num, num - 1, num - 2,,, 1
        #      ^           ^                   ^ (example)
        #   |leftPartNotInc|   rightPartNotInc |
        leftPartNotInc = num - index - 1
        rightPartNotInc = num - (n - index)

        # if leftPartNotInc >= 0 that means sequence on the left side ends normally
        if leftPartNotInc >= 0:
            leftPartSum = maxPartSum - (leftPartNotInc * (leftPartNotInc + 1) // 2)
        # if not then normal sequence ends at 1, and remaining numbers are 1(as all numbers are positive)
        else:
            leftPartSum = maxPartSum + abs(leftPartNotInc)
        
        # same as leftPartSum
        if rightPartNotInc >= 0:
            rightPartSum = maxPartSum - (rightPartNotInc * (rightPartNotInc + 1) // 2)
        else:
            rightPartSum = maxPartSum + abs(rightPartNotInc)

        # total sum = leftPartSum + rightPartSum + num
        return leftPartSum + rightPartSum + num
    
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        low, high = 1, maxSum - n + 1 # only edge case of only 1 element in the array
        ans = low

        while low <= high:
            mid = (low + high) >> 1

            if self.calcNumsSum(n, index, mid) <= maxSum:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
# Time Complexity: O(log(maxSum - n + 1))
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.calcNumsSum(9, 3, 3)) 
