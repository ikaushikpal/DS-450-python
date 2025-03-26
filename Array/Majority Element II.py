class Solution:
    def majorityElement(self, nums):
        value1, value2 =  self.boyerMooreMajorityVoteAlgo(nums)
        count1 = count2 = 0

        for num in nums:
            if num == value1:
                count1 += 1
            
            elif num == value2:
                count2 += 1
        
        res = []
        if count1 > len(nums)//3:
            res.append(value1)

        if value1 != value2 and count2 > len(nums)//3:
            res.append(value2)

        return res

    def boyerMooreMajorityVoteAlgo(self, nums):
        value1, count1 = nums[0], 1
        value2, count2 = nums[0], 0

        for i in range(1, len(nums)):
            if nums[i] == value1:
                count1 += 1
            elif nums[i] == value2:
                count2 += 1
            else:
                if count1 == 0:
                    value1, count1 = nums[i], 1
                elif count2 == 0:
                    value2, count2 = nums[i], 1
                else:
                    count1 -= 1
                    count2 -= 1

        return [value1, value2]


if __name__ == '__main__':
    sol = Solution()

    # Example 1:
    # Input: nums = [3,2,3]
    # Output: [3]
    print(sol.majorityElement([3,2,3]))

    # Example 2:
    # Input: nums = [1]
    # Output: [1]
    print(sol.majorityElement([1]))


    # Example 3:
    # Input: nums = [1,2]
    # Output: [1,2]
    print(sol.majorityElement([1,2]))

    print(sol.majorityElement([3,3,1,1,1,1,2,4,4,3,3,3,4,4]))
    print(sol.majorityElement([2,1,1,3,1,4,5,6]))
