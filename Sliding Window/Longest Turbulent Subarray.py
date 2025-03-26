# Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

# A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

# More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

# For i <= k < j:
# arr[k] > arr[k + 1] when k is odd, and
# arr[k] < arr[k + 1] when k is even.
# Or, for i <= k < j:
# arr[k] > arr[k + 1] when k is even, and
# arr[k] < arr[k + 1] when k is odd.
 

# Example 1:
# Input: arr = [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]


# Example 2:
# Input: arr = [4,8,12,16]
# Output: 2


# Example 3:
# Input: arr = [100]
# Output: 1


from collections import deque
from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        window = deque()
        maxLength = 0
        for num in arr:
            if len(window) & 1:
                while window and window[-1] <= num:
                    window.popleft()
            else:
                while window and window[-1] >= num:
                    window.popleft()
            window.append(num)
            maxLength = max(maxLength, len(window))
        
        window = deque()
        for num in arr:
            if len(window) & 1:
                while window and window[-1] >= num:
                    window.popleft()
            else:
                while window and window[-1] <= num:
                    window.popleft()
            window.append(num)
            maxLength = max(maxLength, len(window))
        return maxLength

if __name__ == "__main__":
    sol = Solution()
    arr = [9,4,2,10,7,8,8,1,9]
    print(sol.maxTurbulenceSize(arr))
    arr = [4,8,12,16]
    print(sol.maxTurbulenceSize(arr))
    arr = [100]
    print(sol.maxTurbulenceSize(arr))
