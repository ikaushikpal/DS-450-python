# Given a sorted array arr[] of size N and an integer K. The task is to check if K is present in the array or not using ternary search.

# Ternary Search- It is a divide and conquer algorithm that can be used to find an element in an array. In this algorithm, we divide the given array into three parts and determine which has the key (searched element).


# Example 1:
# Input:
# N = 5, K = 6
# arr[] = {1,2,3,4,6}
# Output: 1
# Exlpanation: Since, 6 is present in 
# the array at index 4 (0-based indexing),
# output is 1.


# Example 2:
# Input:
# N = 5, K = 2
# arr[] = {1,3,4,5,6}
# Output: -1
# Exlpanation: Since, 2 is not present 
# in the array, output is -1.


class Solution:
    def ternarySearch(self, arr, N, target):
        low, high = 0, N - 1
        
        while low <= high:
            mid1 = low + (high - low) // 3
            mid2 = high - (high - low) // 3
            
            if arr[mid1] == target or arr[mid2] == target:
                return 1
            elif arr[mid1] > target:
                high = mid1 - 1
            elif arr[mid2] < target:
                low = mid2 + 1
            else:
                low = mid1 + 1
                high = mid2 - 1
        return -1
# T.C. = O(log3(N))
# S.C. = O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.ternarySearch([1,2,3,4,6], 5, 6))
    print(sol.ternarySearch([1,3,4,5,6], 5, 2))
    