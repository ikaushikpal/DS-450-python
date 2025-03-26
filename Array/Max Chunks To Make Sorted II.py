# You are given an integer array arr.
# We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.
# Return the largest number of chunks we can make to sort the array.

# Example 1:

# Input: arr = [5,4,3,2,1]
# Output: 1
# Explanation:
# Splitting into two or more chunks will not return the required result.
# For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.

# Example 2:

# Input: arr = [2,1,3,4,4]
# Output: 4
# Explanation:
# We can split into two chunks, such as [2, 1], [3, 4, 4].
# However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.


class Solution:
    def generateRightMin(self, arr):
        rightMin = [float('inf')] * (len(arr) + 1)

        for i in range(len(arr)-1, -1, -1):
            rightMin[i] = min(rightMin[i + 1], arr[i])

        return rightMin

    def maxChunksToSorted(self, arr: list) -> int:
        countChunks = 0
        rightMin = self.generateRightMin(arr)
        maxSoFar = float('-inf')

        for i in range(len(arr)):
            maxSoFar = max(maxSoFar, arr[i])

            if maxSoFar <= rightMin[i + 1]:
                countChunks += 1                
        return countChunks


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxChunksToSorted([5,4,3,2,1]))
    print(sol.maxChunksToSorted([2,1,3,4,4]))
    print(sol.maxChunksToSorted([0, 1, 2, 3, 4]))
