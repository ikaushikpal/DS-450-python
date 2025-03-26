# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.


# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]


# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]


from typing import List


class Solution:
    def helper(self, candidates, i, current, target, currCombi):
        if current == target:
            self.ans.append(currCombi[:])
            return
        
        if current > target:
            return
        
        for j in range(i, len(candidates)):
            # Very important here! We don't use `i > 0` because we always want 
            # to count the first element in this recursive step even if it is the same 
            # as one before. To avoid overcounting, we just ignore the duplicates
            # after the first element.
            if j > i and candidates[j] == candidates[j-1]:
                continue
            
            currCombi.append(candidates[j])
            self.helper(candidates, j+1, current+candidates[j], target, currCombi)
            currCombi.pop()
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        candidates.sort()
        self.helper(candidates, 0, 0, target, [])
        return list(self.ans)
# Time Complexity: O(2^n)
# Space Complexity: O(n)


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum2([10,1,2,7,6,1,5], 8))
    print(sol.combinationSum2([2,5,2,1,2], 5))

