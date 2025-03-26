class Solution:
# @param A : list of integers
# @return an integer
    def findMinXor(self, nums):
        nums.sort()

        x = nums[0]
        minimumXOR = 10**9

        for i in range(1, len(nums)):
            y = nums[i]
            minimumXOR = min(minimumXOR, x^y)
            x = y
        
        return minimumXOR

            
