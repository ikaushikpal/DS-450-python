# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]


# Example 2:
# Input: nums = [1,1]
# Output: [1,2]


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
            else:
                duplicate = index + 1
            
        for i, num in enumerate(nums):
            if num > 0:
                missing = i + 1
                return (duplicate, missing)
        return [0, 0]
# Time Complexity: O(n)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findErrorNums([1,2,2,4]))
    print(sol.findErrorNums([1,1]))