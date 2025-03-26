# Given an array of positive and negative numbers, arrange them in an alternate fashion such that every positive number is followed by negative and vice-versa. Order of elements in output doesn’t matter. Extra positive or negative elements should be moved to end.

# Examples: 

# Input :
# arr[] = {-2, 3, 4, -1}
# Output :
# arr[] = {-2, 3, -1, 4} OR {-1, 3, -2, 4} OR ..

# Input :
# arr[] = {-2, 3, 1}
# Output :
# arr[] = {-2, 3, 1} OR {-2, 1, 3} 

# Input : 
# arr[] = {-5, 3, 4, 5, -6, -2, 8, 9, -1, -4}
# Output :
# arr[] = {-5, 3, -2, 5, -6, 4, -4, 9, -1, 8} 



class Solution:
    def rearrange(self, nums, n):
        # first shift all negative numbers to left
        l = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
            
        # swap-ing
        i = l - 2
        j = l + 1
        while i >= 0 and j < len(nums):
            nums[i], nums[j] = nums[j], nums[i]
            i -= 2
            j += 2
        
    def printArray(self, nums, n):
        print(*nums)
# Time Complexity: O(N)
# Space Complexity : O(1)


if __name__ == '__main__':
    sol = Solution()
    nums = [-2, 3, 4, -1]
    sol.rearrange(nums, 4)
    sol.printArray(nums, 4)


    nums = [-2, 3, 1]
    sol.rearrange(nums, 3)
    sol.printArray(nums, 3)


    nums = [-5, 3, 4, 5, -6, -2, 8, 9, -1, -4]
    sol.rearrange(nums, 8)
    sol.printArray(nums, 8)

    nums = [2, 3, -4, -1, 6, -9]
    sol.rearrange(nums, 6)
    sol.printArray(nums, 6)
