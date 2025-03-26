# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def nodeToRootPath(self, root, targetNode):
        if root is None:
            return []
        
        if root == targetNode:
            return [root]
             
        array = self.nodeToRootPath(root.left, targetNode)
        if len(array) > 0:
            array.append(root)
            return array
        
        array = self.nodeToRootPath(root.right, targetNode)
        if len(array) > 0:
            array.append(root)
            return array
        
        return []

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_list = self.nodeToRootPath(root, p) # returns reversed p node to root node path
        if len(p_list) == 0: return None

        q_list = self.nodeToRootPath(root, q) # returns reversed q node to root node path
        if len(q_list) == 0: return None

        i = len(p_list) - 1
        j = len(q_list) - 1

        while i>=0 and j>=0 and p_list[i] == q_list[j]:
            i -= 1
            j -= 1
        
        if i == -1 and j == -1: return None # if no lca found
        else : return p_list[i+1]
