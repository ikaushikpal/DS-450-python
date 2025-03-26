# You are given two 0-indexed arrays nums and cost consisting each of n positive integers.

# You can do the following operation any number of times:

# Increase or decrease any element of the array nums by 1.
# The cost of doing one operation on the ith element is cost[i].

# Return the minimum total cost such that all the elements of the array nums become equal.

 

# Example 1:
# Input: nums = [1,3,5,2], cost = [2,3,1,14]
# Output: 8
# Explanation: We can make all the elements equal to 2 in the following way:
# - Increase the 0th element one time. The cost is 2.
# - Decrease the 1st element one time. The cost is 3.
# - Decrease the 2nd element three times. The cost is 1 + 1 + 1 = 3.
# The total cost is 2 + 3 + 3 = 8.
# It can be shown that we cannot make the array equal with a smaller cost.


# Example 2:
# Input: nums = [2,2,2,2,2], cost = [4,2,8,1,3]
# Output: 0
# Explanation: All the elements are already equal, so no operations are needed.


class Solution:
    def calcCost(self, nums, cost, x):
        return sum(abs(num - x) * c for num, c in zip(nums, cost))
    
    def minCost(self, nums, cost):
        left, right = min(nums), max(nums)
        res = self.calcCost(nums, cost, nums[0])
        
        while left < right:
            x = (left + right) >> 1
            
            y1 = self.calcCost(nums, cost, x)
            y2 = self.calcCost(nums, cost, x + 1)
            
            res = min(y1, y2)
            
            if y1 < y2:
                right = x
            else:
                left = x + 1
                
        return res
# Time Complexity: O(nlogn)
# Space Complexity: O(1)

# https://leetcode.com/problems/minimum-cost-to-make-array-equal/discuss/2734162/JavaC%2B%2BPython-Binary-Search
# https://leetcode.com/problems/minimum-cost-to-make-array-equal/discuss/2734728/Pure-math-based-explanation-of-why-Cost-Function-is-convex

if __name__ == '__main__':
    sol = Solution()
    print(sol.minCost([1,3,5,2], [2,3,1,14]))
    print(sol.minCost([2,2,2,2,2], [4,2,8,1,3]))