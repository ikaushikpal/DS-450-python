# Given two binary max heaps as arrays, merge the given heaps to form a new max heap.


# Example 1:
# Input  : 
# n = 4 m = 3
# a[] = {10, 5, 6, 2}, 
# b[] = {12, 7, 9}
# Output : 
# {12, 10, 9, 2, 5, 7, 6}


from heapq import heapify


class Solution():
    def mergeHeaps(self, arr1, arr2, N, M):
        for i in range(N):
            arr1[i] *= -1
        
        for i in range(M):
            arr2[i] *= -1
        
        arr3 = arr1 + arr2
        heapify(arr3)
        
        for i in range(N + M):
            arr3[i] *= -1
        
        return arr3
# Time Complexity : (N + M)
# Space Complexity : (N + M)


if __name__ == '__main__':
    sol = Solution()
    print(sol.mergeHeaps([10, 5, 6, 2], [12, 7, 9], 4, 3))