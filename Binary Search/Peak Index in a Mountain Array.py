# An array arr a mountain if the following properties hold:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

# You must solve it in O(log(arr.length)) time complexity.


# Example 1:
# Input: arr = [0,1,0]
# Output: 1


# Example 2:
# Input: arr = [0,2,1,0]
# Output: 1


# Example 3:
# Input: arr = [0,10,5,2]
# Output: 1


from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        N = len(arr)
        low, high = 0, N - 1
        
        while low <= high:
            mid = (low + high) >> 1
            
            cond1 = mid == 0 or arr[mid - 1] < arr[mid]
            cond2 = mid == N - 1 or arr[mid] > arr[mid + 1]
            
            if cond1 and cond2:
                return mid
            elif mid != N - 1 and arr[mid] > arr[mid + 1]:
                high = mid - 1
            else:
                low = mid + 1
        return -1
# Time Complexity: O(logN)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.peakIndexInMountainArray(arr = [0,1,0]))
    print(sol.peakIndexInMountainArray(arr = [0,2,1,0]))
    print(sol.peakIndexInMountainArray(arr = [0,10,5,2]))
