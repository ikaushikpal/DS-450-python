# A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

# Design an algorithm to insert a new node to a complete binary tree keeping it complete after the insertion.

# Implement the CBTInserter class:

# CBTInserter(TreeNode root) Initializes the data structure with the root of the complete binary tree.
# int insert(int v) Inserts a TreeNode into the tree with value Node.val == val so that the tree remains complete, and returns the value of the parent of the inserted TreeNode.
# TreeNode get_root() Returns the root node of the tree.
 

# Example 1:
# Input
# ["CBTInserter", "insert", "insert", "get_root"]
# [[[1, 2]], [3], [4], []]
# Output
# [null, 1, 2, [1, 2, 3, 4]]

# Explanation
# CBTInserter cBTInserter = new CBTInserter([1, 2]);
# cBTInserter.insert(3);  // return 1
# cBTInserter.insert(4);  // return 2
# cBTInserter.get_root(); // return [1, 2, 3, 4]


# Constraints:
# The number of nodes in the tree will be in the range [1, 1000].
# 0 <= Node.val <= 5000
# root is a complete binary tree.
# 0 <= val <= 5000
# At most 104 calls will be made to insert and get_root



# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)
        
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.tree = [None]
        self.copy_tree(root)
        
    def copy_tree(self, root):
        # level order
        queue = deque([root])
        while queue:
            node = queue.popleft()

            self.tree.append(node)

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        

    def insert(self, val: int) -> int:
        node = TreeNode(val)

        self.tree.append(node)

        parent_index = (len(self.tree) - 1) // 2
        parent = self.tree[parent_index]

        if not parent:
            return None
        
        if not parent.left:
            parent.left = node
        else:
            parent.right = node    

        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.tree[1]


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()


if __name__ == '__main__':
    t = TreeNode(1)
    t.left = TreeNode(2)

    obj = CBTInserter(t)
    print(obj.insert(3))
    print(obj.insert(4))
    print(obj.get_root())