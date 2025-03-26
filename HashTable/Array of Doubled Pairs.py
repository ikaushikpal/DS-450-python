# Given an integer array of even length arr, return true if it is possible to reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, or false otherwise.
 

# Example 1:
# Input: arr = [3,1,3,6]
# Output: false


# Example 2:
# Input: arr = [2,1,2,6]
# Output: false


# Example 3:
# Input: arr = [4,-2,2,-4]
# Output: true
# Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].


from typing import List


class Solution:
    def helper(self, nums):
        visited = {}
        maxLength = 0

        for num in nums:
            prevNum = num // 2
            if prevNum in visited:
                visited[num] = 1 + visited[prevNum]
            else:
                visited[num] = 1
            maxLength = max(maxLength, visited[num])
        
        return maxLength

    def canReorderDoubled(self, arr: List[int]) -> bool:
        positives = []
        negatives = []

        for val in arr:
            if val < 0:
                negatives.append(val)
            elif val > 0:
                positives.append(val)
            else: 
                negatives.append(val)
                positives.append(val)
        
        positives.sort()
        if self.helper(positives) > len(arr)//2:
            return True
        
        negatives.sort(reverse=True)
        if self.helper(negatives) > len(arr)//2:
            return True
        
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.canReorderDoubled([3,1,3,6]))
    print(sol.canReorderDoubled([2,1,2,6]))
    print(sol.canReorderDoubled([4,-2,2,-4]))
