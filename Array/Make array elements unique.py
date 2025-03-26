# Given an array arr[ ] of N elements, your task is to find the minimum number of increment operations required to make all the elements of the array unique. ie- no value in the array should occur more than once. In an operation a value can be incremented by 1 only.


# Example 1:
# Input:
# N = 3
# arr[] = {1, 2, 2}
# Output:
# 1
# Explanation:
# If we increase arr[2] by 1 then the resulting 
# array becomes {1, 2, 3} and has all unique values.
# Hence, the answer is 1 in this case.


# Example 2:
# Input: 
# N = 4
# arr[] = {1, 1, 2, 3}
# Output:
# 3
# Explanation: 
# If we increase arr[0] by 3, then all array
# elements will be unique. Hence, the answer 
# is 3 in this case.


class Solution:
    def minIncrements(self, arr, N): 
        arr.sort()
        counter = arr[0] + 1
        ans = 0
        
        for i in range(1, N):
            if arr[i] >= counter:
                counter = arr[i] + 1
            else:
                diff = counter - arr[i]
                ans += diff
                counter += 1
        return ans
# Time complexity: O(NlogN)
# Space complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minIncrements([1, 2, 2], 3))
    print(sol.minIncrements([1, 1, 2, 3], 4))