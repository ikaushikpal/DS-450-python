class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    # Return True if the given trees are isomomorphic. Else return False.
    def isIsomorphic(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        
        elif root1 is None or root2 is None:
            return False

        elif root1.data != root2.data:
            return False

        return (self.isIsomorphic(root1.left, root2.left) & self.isIsomorphic(root1.right, root2.right)) |\
                (self.isIsomorphic(root1.left, root2.right) & self.isIsomorphic(root1.right, root2.left))


        