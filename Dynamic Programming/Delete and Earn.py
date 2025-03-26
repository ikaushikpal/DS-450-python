# You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of times.


# Example 1:
# Input: nums = [3,4,2]
# Output: 6
# Explanation: You can perform the following operations:
# - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
# - Delete 2 to earn 2 points. nums = [].
# You earn a total of 6 points.


# Example 2:
# Input: nums = [2,2,3,3,3,4]
# Output: 9
# Explanation: You can perform the following operations:
# - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
# - Delete a 3 again to earn 3 points. nums = [3].
# - Delete a 3 once more to earn 3 points. nums = [].
# You earn a total of 9 points.


from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = Counter(nums)
        nums = sorted(list(set(nums)))
        # here we are using two variables to store dp[i-2] and dp[i-1] values
        # where earn1 is dp[i-2] and earn2 is dp[i-1]
        # maxEarn is our overall answer
        earn1 = earn2 = 0
        
        # main idea to propagate maxEarn using earn2
        for i, num in enumerate(nums):
            # num can earn by itself
            currEarn = num * freq[num]
            
            # lets say nums = [..., 7, 8, 9, ...]
            # now num is 9, so we can not take dp[i-1] because it is just adjacent
            # but we can take 7
            if i > 0 and nums[i-1] + 1 == nums[i]:
                newEarn = max(currEarn + earn1, earn2)
            else:
                # lets say nums = [..., 7, 8, 10, ....]
                # now num is 10, 10 can be paired with 8 and 7
                # so taking maximum earn
                newEarn = currEarn + max(earn1, earn2)
            
            # propagating earn1 and earn2
            earn1, earn2 = earn2, newEarn
        
        # earn2 is now dp[-1]
        return earn2
# Time Complexity: O(NlogN)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.deleteAndEarn([3,4,2]))
    print(sol.deleteAndEarn([2,2,3,3,3,4]))