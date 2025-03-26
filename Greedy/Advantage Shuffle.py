# You are given two integer arrays nums1 and nums2 both of the same length. The advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].

# Return any permutation of nums1 that maximizes its advantage with respect to nums2.


# Example 1:
# Input: nums1 = [2,7,11,15], nums2 = [1,10,4,11]
# Output: [2,11,7,15]


# Example 2:
# Input: nums1 = [12,24,8,32], nums2 = [13,25,32,11]
# Output: [24,32,8,12]



from typing import List
from copy import deepcopy
from collections import defaultdict


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2Copy = deepcopy(nums2)
        nums2Copy.sort()
        nums1.sort()
        unMappedNums = list()
        mappedNums = defaultdict(list)

        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2Copy[j]:
                mappedNums[nums2Copy[j]].append(nums1[i])
                j += 1
            else:
                unMappedNums.append(nums1[i])
            i += 1
        
        res = []
        for i in range(len(nums1)):
            num = nums2[i]
            if num in mappedNums and len(mappedNums[num]) > 0:
                res.append(mappedNums[num].pop())
            else:
                res.append(unMappedNums.pop())
        return res
# Time Complexity: O(NlogN)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.advantageCount([2,7,11,15], [1,10,4,11]))
    print(sol.advantageCount([12,24,8,32], [13,25,32,11]))
    print(sol.advantageCount([2,0,4,1,2],[1,3,0,0,2]))
