# Given an integer array a[ ] of N elements and an integer K, the task is to check if the array a[ ] could be divided into K non-empty subsets with equal sum of elements.
# Note: All elements of this array should be part of exactly one partition.

# Example 1:
# Input: 
# N = 5
# a[] = {2,1,4,5,6}
# K = 3
# Output: 
# 1
# Explanation: we can divide above array 
# into 3 parts with equal sum as (2, 4), 
# (1, 5), (6)


# Example 2:
# Input: 
# N = 5 
# a[] = {2,1,5,5,6}
# K = 3
# Output: 
# 0
# Explanation: It is not possible to divide
# above array into 3 parts with equal sum.





class Solution:
    def isAnswer(self, partitions, target):
        for i in range(len(partitions)):
            if partitions[i] != target and partitions[i] == 0:
                return False
        return True

    def helper(self, arr, i, partitions, target):
        if i == -1:
            return self.isAnswer(partitions, target)
        
        for k in range(len(partitions)):
            if partitions[k] + arr[i] <= target:
                partitions[k] += arr[i]
                if self.helper(arr, i-1, partitions, target):
                    return True
                partitions[k] -= arr[i]
        return False

    def isKPartitionPossible(self, arr, k):
        total = sum(arr)
        if total % k != 0:
            return False
        target = total // k
        partitions = [0] * k
        return self.helper(arr, len(arr)-1, partitions, target)
# Time Complexity: O(K^N)
# Space Complexity: O(K)


if __name__ == '__main__':
    sol = Solution()
    print(sol.isKPartitionPossible([2,1,4,5,6], 3))
    print(sol.isKPartitionPossible([2,1,5,5,6], 3))