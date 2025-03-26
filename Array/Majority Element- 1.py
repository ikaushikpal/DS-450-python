# Moore's Voting Algorithm(1991)

# Problem Statement :
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.
# Example 1:

# Input: nums = [3,2,3]
# Output: 3

# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

class Solution:
    def majorityELement(self, nums):
        possibleValue = self.mooreVotingAlgo(nums)
        # if problem statement says that every array has a majority element
        # then simply return possibleValue
        # else we need to count frequency of possibleValue and check if that
        # is greater than len(nums) // 2 or not; if not return someting else
        # to denote that given array do not contain any majority element

        frequency = 0
        for num in nums:
            if num == possibleValue:
                frequency += 1

        if frequency > len(nums) // 2:
            return possibleValue
        else:
            return None

    def mooreVotingAlgo(self, nums):
        # initial
        value, count = nums[0], 1

        for i in range(1, len(nums)):
            # if nums[i] same as value then increment frequency
            if nums[i] == value:
                count += 1

            # else we need to pair nums[i] with value
            # paring is nothing but saying that value's
            # frequency decremented
            else:
                count -= 1

            # if count == 0 meaning nums[i] can be potential element
            if count == 0:
                value, count = nums[i], 1

        return value


if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityELement([3, 2, 3]))  # O/P : 3
    print(sol.majorityELement([2, 2, 1, 1, 1, 2, 2]))  # O/P : 2
    print(sol.majorityELement([3, 2, 1]))  # O/P : None
