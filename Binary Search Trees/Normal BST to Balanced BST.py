# Given a Binary Search Tree, modify the given BST such that itis balanced and has minimum possible height.

# Examples :

# Input:
#        30
#       /
#      20
#     /
#    10

# Output:
#      20
#    /   \
#  10     30

# Input:
#          4
#         /
#        3
#       /
#      2
#     /
#    1

# Output:
#       3            3           2
#     /  \         /  \        /  \
#    1    4   OR  2    4  OR  1    3   OR ..
#     \          /                   \
#      2        1                     4 


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def storeInorder(self, root, inorder):
        if root is None:
            return
        
        self.storeInorder(root.left, inorder)
        inorder.append(root.data)
        self.storeInorder(root.right, inorder)

    def buildBST(self, low, high, inorder):
        if low > high:
            return None
        
        mid = (low + high) // 2
        root = Node(inorder[mid])
        
        root.left = self.buildBST(low, mid - 1, inorder)
        root.right = self.buildBST(mid + 1, high, inorder)
        
        return root

    def buildBalancedTree(self,root):
        inorder = []
        self.storeInorder(root, inorder)
        return self.buildBST(0, len(inorder)-1, inorder)


if __name__ == '__main__':
    root = Node(4)
    root.left = Node(3)
    root.left.left = Node(2)
    root.left.left.left = Node(1)

    sol = Solution()
    print(sol.buildBalancedTree(root))