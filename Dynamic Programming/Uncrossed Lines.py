# You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

# We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

# nums1[i] == nums2[j], and
# the line we draw does not intersect any other connecting (non-horizontal) line.
# Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

# Return the maximum number of connecting lines we can draw in this way.

 

# Example 1:
# Input: nums1 = [1,4,2], nums2 = [1,2,4]
# Output: 2
# Explanation: We can draw 2 uncrossed lines as in the diagram.
# We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.


# Example 2:
# Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
# Output: 3


# Example 3:
# Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
# Output: 2


from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        N, M = len(nums1), len(nums2)
        
        if N < M:
            return self.maxUncrossedLines(nums2, nums1)
        
        prevDp = [0] * (M+1) 
        ans = 0
        
        for i in range(1, N + 1):
            currDp = [0] * (M + 1)
            
            for j in range(1, M + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    currDp[j] = prevDp[j - 1] + 1
                else:
                    currDp[j] = max(currDp[j - 1], prevDp[j])
                
                ans = max(ans, currDp[j])
            prevDp = currDp
        return ans
# Time complexity: O(N*M)
# Space complexity: O(M)


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxUncrossedLines([1,4,2], [1,2,4]))
    print(sol.maxUncrossedLines([2,5,1,2,5], [10,5,2,1,5,2]))
    print(sol.maxUncrossedLines([1,3,7,1,7,5], [1,9,2,5,1]))
