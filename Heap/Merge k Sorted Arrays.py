# Given k sorted arrays arranged in the form of a matrix of size k * k. The task is to merge them into one sorted array. Return the merged sorted array ( as a pointer to the merged sorted arrays in cpp, as an ArrayList in java, and list in python).


# Examples :

# Example 1:
# Input: k = 3, arr[][] = {{1,2,3},{4,5,6},{7,8,9}}
# Output: 1 2 3 4 5 6 7 8 9
# Explanation: Above test case has 3 sorted arrays of size 3, 3, 3 arr[][] = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]. The merged list will be [1, 2, 3, 4, 5, 6, 7, 8, 9].

# Example 2:
# Input: k = 4, arr[][]={{1,2,3,4},{2,2,3,4},{5,5,6,6},{7,8,9,9}}
# Output: 1 2 2 2 3 3 4 4 5 5 6 6 7 8 9 9 
# Explanation: Above test case has 4 sorted arrays of size 4, 4, 4, 4 arr[][] = [[1, 2, 2, 2], [3, 3, 4, 4], [5, 5, 6, 6], [7, 8, 9, 9 ]]. The merged list will be [1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 9].

# Expected Time Complexity: O(k2*Log(k))
# Expected Auxiliary Space: O(k2)

# Constraints:
# 1 <= k <= 100



import heapq


class Solution:
    def mergeKArrays(self, arr, K):
        # question is very similar to merge K sorted LL
        min_heap = []
        for i, row in enumerate(arr):
            # (value, #which row, #index of that row)
            min_heap.append((row[0], i, 0)) 

        heapq.heapify(min_heap)
        ans = []

        while min_heap:
            value, row_index, index = heapq.heappop(min_heap)

            if index + 1 < len(arr[row_index]):
                heapq.heappush(min_heap, (arr[row_index][index + 1], row_index, index + 1))

            ans.append(value)
        return ans
# Time Complexity: O(k^2*Log(k))
# Auxiliary Space: O(k^2)


if __name__ == '__main__':
    sol = Solution()
    print(sol.mergeKArrays([[1,2,3],[4,5,6],[7,8,9]], 3))
    print(sol.mergeKArrays([[1,2,3,4],[2,2,3,4],[5,5,6,6],[7,8,9,9]], 4))