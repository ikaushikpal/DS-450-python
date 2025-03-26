# Given two BSTs, return elements of both BSTs in sorted form.


# Example 1:
# Input:
# BST1:
#        5
#      /   \
#     3     6
#    / \
#   2   4  
# BST2:
#         2
#       /   \
#      1     3
#             \
#              7
#             /
#            6
# Output: 1 2 2 3 3 4 5 6 6 7
# Explanation: 
# After merging and sorting the
# two BST we get 1 2 2 3 3 4 5 6 6 7.


# Example 2:
# Input:
# BST1:
#        12
#      /   
#     9
#    / \    
#   6   11
# BST2:
#       8
#     /  \
#    5    10
#   /
#  2
# Output: 2 5 6 8 9 10 11 12
# Explanation: 
# After merging and sorting the
# two BST we get 2 5 6 8 9 10 11 12.


class Solution:
    def storeInorder(self, root, nums):
        if root is None:
            return
        
        self.storeInorder(root.left, nums)
        nums.append(root.data)
        self.storeInorder(root.right, nums)
    
    def mergeSortedArrays(self, arr1, arr2):
        arr3 = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                arr3.append(arr1[i])
                i += 1
            else:
                arr3.append(arr2[j])
                j += 1
        
        arr3.extend(arr1[i:])
        arr3.extend(arr2[j:])
        return arr3
        
    def merge(self, root1, root2):
        numsFirst, numsSecond = [], []
        self.storeInorder(root1, numsFirst)
        self.storeInorder(root2, numsSecond)
        return self.mergeSortedArrays(numsFirst, numsSecond)
# Time Complexity: O(n + m)
# Space Complexity: O(h1 + h2)