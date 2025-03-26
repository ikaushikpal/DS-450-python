# The array-form of an integer num is an array representing its digits in left to right order.

# For example, for num = 1321, the array form is [1,3,2,1].
# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

 
# Example 1:
# Input: num = [1,2,0,0], k = 34
# Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234


# Example 2:
# Input: num = [2,7,4], k = 181
# Output: [4,5,5]
# Explanation: 274 + 181 = 455


# Example 3:
# Input: num = [2,1,5], k = 806
# Output: [1,0,2,1]
# Explanation: 215 + 806 = 1021


from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        N = len(num)
        ans = []
        i = N - 1
        
        while i >= 0 or k > 0:
            if i >= 0:
                k += num[i]
                i -= 1
            
            ans.append(k % 10)
            k = k // 10
        return ans[::-1]
# Time Complexity: O(max(N, log k))
# Space Complexity: O(max(N, log k))


if __name__ == '__main__':
    sol = Solution()
    print(sol.addToArrayForm(num = [1,2,0,0], k = 34))
    print(sol.addToArrayForm(num = [2,7,4], k = 181))
    print(sol.addToArrayForm(num = [2,1,5], k = 806))