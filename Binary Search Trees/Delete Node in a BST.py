from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSucc(self, root):
        root = root.right
        
        while root and root.left:
            root = root.left
            
        return root.val
    
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        else: #found key Node
            
            # check if node is leaf
            if not root.left and not root.right:
                return None
            
            # one child
            if root.left and not root.right:
                root = root.left
            
            elif not root.left and root.right:
                root = root.right
            
            # both child
            else:
                succ = self.findSucc(root)
                root.val = succ
                
                root.right =  self.deleteNode(root.right, root.val)
                        
                    
        return root


if __name__ == '__main__':
    pass