# Given an array arr[] of distinct integers of size N and a value sum, the task is to find the count of triplets (i, j, k), having (i<j<k) with the sum of (arr[i] + arr[j] + arr[k]) smaller than the given value sum.


# Example 1:
# Input: N = 4, sum = 2
# arr[] = {-2, 0, 1, 3}
# Output:  2
# Explanation: Below are triplets with 
# sum less than 2 (-2, 0, 1) and (-2, 0, 3). 
 

# Example 2:
# Input: N = 5, sum = 12
# arr[] = {5, 1, 3, 4, 7}
# Output: 4
# Explanation: Below are triplets with 
# sum less than 12 (1, 3, 4), (1, 3, 5), 
# (1, 3, 7) and (1, 4, 5).


class Solution:
    def countTriplets(self, arr, n, target):
        arr.sort()
        count = 0
        
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                if arr[i] + arr[j] + arr[k] < target:
                    count += (k - j)
                    j += 1
                else:
                    k -= 1
        
        return count
# Time Complexity: O(N^2)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countTriplets([-2, 0, 1, 3], 4, 2))
    print(sol.countTriplets([5, 1, 3, 4, 7], 5, 12))
    