# Note: We are considering that BSTs can not contain duplicate Nodes.
# meaing non inclusive range

class Solution:
    
    def isBSTUtil(self, root, left_range, right_range):
        if self.FLAG == False:
            return False
        
        if root is None:
            return True

        left = self.isBSTUtil(root.left, left_range, root.data)
        if left == False:
            self.FLAG = False
            return False

        right = self.isBSTUtil(root.right, root.data, right_range)
        if right == False:
            self.FLAG = False
            return False

        if left_range < root.data < right_range:
            return True
        else:
            return False

    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        self.FLAG = True
        self.isBSTUtil(root, float('-inf'), float('inf'))

        return self.FLAG