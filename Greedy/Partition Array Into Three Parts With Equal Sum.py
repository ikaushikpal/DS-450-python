# Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

# Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

 

# Example 1:
# Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1


# Example 2:
# Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false


# Example 3:
# Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
# Output: true
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4


from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        
        avg = total // 3
        validParts = cumm = 0
        for val in arr:
            cumm += val
            if cumm == avg:
                validParts += 1
                cumm = 0
        
        return validParts >= 3
# Time Complexity : O(N)
# Space Complexity : O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))