# You are given an array of integers nums and an integer target.

# Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.

 

# Example 1:
# Input: nums = [3,5,6,7], target = 9
# Output: 4
# Explanation: There are 4 subsequences that satisfy the condition.
# [3] -> Min value + max value <= target (3 + 3 <= 9)
# [3,5] -> (3 + 5 <= 9)
# [3,5,6] -> (3 + 6 <= 9)
# [3,6] -> (3 + 6 <= 9)


# Example 2:
# Input: nums = [3,3,6,8], target = 10
# Output: 6
# Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
# [3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]


# Example 3:
# Input: nums = [2,3,3,4,6,7], target = 12
# Output: 61
# Explanation: There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
# Number of valid subsequences (63 - 2 = 61).


from typing import List


class Solution:
    def findFloor(self, arr, low, high, key):
        res = -1

        while low <= high:
            mid = (low+high)//2
            
            if arr[mid] <= key:
                res = mid
                low = mid + 1
            
            else:
                high = mid - 1

        return res
    
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        
        for i in range(len(nums)):
            req = target - nums[i]
            if req < 0:
                break
                
            pos = self.findFloor(nums, i, len(nums)-1, req)
            if pos == -1:
                break
                
            ans += 1 << (pos - i)
        
        return ans % 1000_000_007
        

if __name__ == '__main__':
    sol = Solution()
    print(sol.numSubseq([7,10,7,3,7,5,4], 12))
    print(sol.numSubseq([2,3,3,4,6,7], 12))
    print(sol.numSubseq([3,3,6,8], 10))
    print(sol.numSubseq([3,5,6,7], 9))