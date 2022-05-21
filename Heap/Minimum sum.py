# Given an array Arr of size N such that each element is from the range 0 to 9. Find the minimum possible sum of two numbers formed using the elements of the array. All digits in the given array must be used to form the two numbers.


# Example 1:
# Input:
# N = 6
# Arr[] = {6, 8, 4, 5, 2, 3}
# Output: 604
# Explanation: The minimum sum is formed 
# by numbers 358 and 246.


# Example 2:
# Input:
# N = 5
# Arr[] = {5, 3, 0, 7, 4}
# Output: 82
# Explanation: The minimum sum is 
# formed by numbers 35 and 047.


import heapq


class Solution:
    def solve(self, arr, n):
        num1 = num2 = 0
        heapq.heapify(arr)

        while arr:
            num = heapq.heappop(arr)
            num1 = num1*10 + num

            if arr:
                num = heapq.heappop(arr)
                num2 = num2 * 10 + num
        
        return num1 + num2
# Time Complexity : O(NlogN)
# Space Complexity: O (1)
# Time taken = 3.38 sec


class Solution:
    def solve(self, arr, n):
        num1 = num2 = 0
        arr.sort()

        for i in range(0, len(arr), 2):
            num1 = num1 * 10 + arr[i]
        
        for i in range(1, len(arr), 2):
            num2 = num2 * 10 + arr[i]
        
        return num1 + num2
# Time taken = 2.53 sec


if __name__ == '__main__':
    sol = Solution()
    print(sol.solve([6, 8, 4, 5, 2, 3], 6))
    print(sol.solve([5, 3, 0, 7, 4], 5))