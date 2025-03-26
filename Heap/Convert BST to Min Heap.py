from heapq import heapify


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
class Solution:
    def storeData(self, root, nums):
        if root is None:
            return
        
        nums.append(root.data)
        self.storeData(root.left, nums)
        self.storeData(root.right, nums)

    def replaceData(self, root, index, nums):
        if root is None:
            return
        
        if index > len(nums):
            return

        root.data = nums[index]
        self.replaceData(root.left, 2*index + 1, nums)
        self.replaceData(root.right, 2*index + 2, nums)

    def convertToMinHeapUtil(self, root):
        nums = []
        self.storeData(root, nums)
        heapify(nums)
        self.replaceData(root, 0, nums)
        return root

# utility +++++++++
def preorderTraversal(root):
    if root == None:
        return
    print(root.data, end=" ")
    preorderTraversal(root.left)
    preorderTraversal(root.right)
 
 
# Driver Code
if __name__ == '__main__':
 
    # BST formation
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)
 
    root = Solution().convertToMinHeapUtil(root)
    print("Preorder Traversal:")
    preorderTraversal(root)