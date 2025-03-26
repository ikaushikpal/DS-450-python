# You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.

# Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.

# Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.

 

# Example 1:
# Input: nums = [10,1,2,7,1,3], p = 2
# Output: 1
# Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5. 
# The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.


# Example 2:
# Input: nums = [4,2,1,2], p = 1
# Output: 0
# Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.

# NOTE:
# There are many good answers binary search + greedy now. I will just explain why greedy works for this problem.

# Imagine you have [a,b,c,d], abcd are just sorted numbers

# Greedy tells us if b - a < the threshold we set, we just pick it. The cost of doing this is if c - b < threshold as well, you can never pick bc pair anymore because b has been paired with a.

# Will this cause any problems?

# The answer is no

# Because if you pick ab pair, you will have one pair now. If you pick bc pair, you also have one pair, however, if you pick bc now what's left is [a, d]. Because we have sorted abcd, d - a is likely to be bigger so it is more likely to exceed the threshold we set.
# On the other hand, if we greedily pick ab pair, what's left is [c,d] and d - c is guaranteed to be smaller or equal to d - a, so d-c is more likely to be a pair that we can pick as well -> being greedy (pick a and b) is more likely to let us have more pairs then not being greedy (pick b and c). Hence for this problem, greedy works for this problem.

from typing import List


class Solution:
    def countPairs(self, nums, diffThreshold, remainingPair):
        i = 1
        #  greedily pick pairs
        while i < len(nums) and remainingPair > 0:
            if nums[i] - nums[i - 1] <= diffThreshold:
                i += 1 # you have picked i and i - 1, you can't pick [i + 1, i] pair anymore
                remainingPair -= 1
            i += 1
        return remainingPair == 0
        
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        
        nums.sort()
        low, high = 0, nums[-1] - nums[0]
        
        
        while low < high:
            mid = low + ((high - low) >> 1)
            
            # check how many pairs we can pick with this threshold(mid)
            if self.countPairs(nums, mid, p):
                high = mid #  we are being to loose on the threshold and have too many pairs, be more strict on the threshold
            else:
                low = mid + 1 # we are being too strict about threshold and we do not have enough pairs, be more loose on threshold
        return low
# Time complexity: O(NlogN)
# Space Complexity: O(1) 


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimizeMax(nums = [10,1,2,7,1,3], p = 2))
    print(sol.minimizeMax([4,2,1,2], 1))
    print(sol.minimizeMax([2,6,2,4,2,2,0,2], 4))