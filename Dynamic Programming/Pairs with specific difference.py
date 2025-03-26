# Given an array of integers, arr[] and a number, K.You can pair two numbers of the array if the difference between them is strictly less than K. The task is to find the maximum possible sum of such disjoint pairs (i.e., each element of the array can be used at most once). The Sum of P pairs is the sum of all 2P elements of pairs.

 

# Example 1:
# Input  : 
# arr[] = {3, 5, 10, 15, 17, 12, 9}
# K = 4
# Output : 
# 62
# Explanation :
# Then disjoint pairs with difference less
# than K are, (3, 5), (10, 12), (15, 17)
# max sum which we can get is 
# 3 + 5 + 10 + 12 + 15 + 17 = 62
# Note that an alternate way to form 
# disjoint pairs is,(3, 5), (9, 12), (15, 17)
# but this pairing produces less sum.
 

# Example 2:
# Input  : 
# arr[] = {5, 15, 10, 300}
# K = 12
# Output : 
# 25


class Solution:
    def maxSumPairWithDifferenceLessThanK(self, arr, N, K): 
        arr.sort()
        total, i = 0, N - 1
        
        while i > 0:
            if arr[i] - arr[i-1] < K:
                total += arr[i] + arr[i - 1]
                i -= 1
            else:
                i -= 1
        
        return total
# Time Complexity: O(NlogN)
# Space Complexity: O(1)


if __name__ == '__main__':
    s = Solution()
    print(s.maxSumPairWithDifferenceLessThanK([3, 5, 10, 15, 17, 12, 9], 7, 4))
    print(s.maxSumPairWithDifferenceLessThanK([5, 15, 10, 300], 4, 12))