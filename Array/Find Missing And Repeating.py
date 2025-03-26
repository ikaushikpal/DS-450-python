# Given an unsorted array Arr of size N of positive integers. One number 'A' from set {1, 2, …N} is missing and one number 'B' occurs twice in array. Find these two numbers.



# Example 1:
# Input:
# N = 2
# Arr[] = {2, 2}
# Output: 2 1
# Explanation: Repeating number is 2 and 
# smallest positive missing number is 1.


# Example 2:
# Input:
# N = 3
# Arr[] = {1, 3, 3}
# Output: 3 2
# Explanation: Repeating number is 3 and 
# smallest positive missing number is 2.


class Solution:
    def findTwoElement(self, arr, N):
        repeatedValue = missingValue = 0

        for i in range(N):
            if arr[abs(arr[i])-1] > 0:
                arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
            else:
                repeatedValue = abs(arr[i])

        for i in range(N):
            if arr[i] > 0:
                missingValue = i + 1
                return (repeatedValue, missingValue)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findTwoElement([13, 33, 43, 16, 25, 19, 23, 31, 29, 35, 10, 2, 32, 11, 47, 15, 34, 46, 30, 26,
          41, 18, 5, 17, 37, 39, 6, 4, 20, 27, 9, 3, 8, 40, 24, 44, 14, 36, 7, 38, 12, 1, 42, 12, 28, 22, 45], 47))
