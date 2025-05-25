# You're given a binary tree. Your task is to find the size of the largest subtree within this binary tree that also satisfies the properties of a Binary Search Tree (BST). The size of a subtree is defined as the number of nodes it contains.

# Note: A subtree of the binary tree is considered a BST if for every node in that subtree, the left child is less than the node, and the right child is greater than the node, without any duplicate values in the subtree.

# Examples :

# Example 1:
# Input: root = [5, 2, 4, 1, 3]
# Root-to-leaf-path-sum-equal-to-a-given-number-copy
# Output: 3
# Explanation:The following sub-tree is a BST of size 3
# Balance-a-Binary-Search-Tree-3-copy

# Example 2:
# Input: root = [6, 7, 3, N, 2, 2, 4]
# Output: 3
# Explanation: The following sub-tree is a BST of size 3:

# Constraints:
# 1 ≤ number of nodes ≤ 10^5
# 1 ≤ node->data ≤ 10^5


class NodeInfo:

    def __init__(self,
                minVal=float('inf'),
                maxVal=float('-inf'),
                isBst=True,
                root=None,
                size=0):

        self.min = minVal
        self.max = maxVal
        self.isBST = isBst
        self.head = root
        self.size = size


class Solution:
    def largestBst_util(self, root)->NodeInfo:
        if root is None:
            return NodeInfo()
        
        left = self.largestBst_util(root.left)
        right = self.largestBst_util(root.right)

        currentNodeInfo = NodeInfo()

        # setting min first
        currentNodeInfo.min = min(root.data, left.min, right.min)

        # max 
        currentNodeInfo.max = max(root.data, left.max, right.max)

        # checking whether is current node is a BST
        # first checking if left sub tree and right sub tree is BST first
        # because if left or right anyone of them is not BST then current root cannot be a BST

        isCapable = left.isBST & right.isBST

        if isCapable == True: # meaning left and right subtree both BST
            # now check if current node is BST

            currentNodeInfo.isBST = root.data > left.max and root.data < right.min

        else:
            currentNodeInfo.isBST = False


        # now finding maximum size BST subtree among left  right and current

        if currentNodeInfo.isBST == True: # if current node is BST then only it is capable of being root
            currentNodeInfo.head = root
            currentNodeInfo.size = left.size + right.size + 1
        
        elif left.size > right.size:
            currentNodeInfo.head = left.head
            currentNodeInfo.size = left.size

        else:
            currentNodeInfo.head = right.head
            currentNodeInfo.size = right.size

        return currentNodeInfo
        

    # Return the size of the largest sub-tree which is also a BST
    def largestBst(self, root):
        treeInfo = self.largestBst_util(root)
        return treeInfo.size
# Time Complexity: O(N)
# Space Complexity: O(H)
