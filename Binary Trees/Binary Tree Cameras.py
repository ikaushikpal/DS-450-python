class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCoverUtil(self, root):
        # state 0 = node buys camera for itself
        # state -1 = node need camera
        # state 1 = node don't need camera
        
        # base case:
        # if root is none then why buy cameras ? So no need camera covered
        if root is None:
            return 1 
        
        left = self.minCameraCoverUtil(root.left)
        right = self.minCameraCoverUtil(root.right)

        if left==-1 or right==-1: # if any child need camera then need to buy camera
            self.countCameras += 1
            return 0
        
        elif left == 0 or right == 0: # if any child have camera for themselves then parent don't need to camera
            return 1                  # because its child will monitor itself 
        
        else:
            return -1 # need to camera to monitor itself and it's both child already been monitored             
        

    def minCameraCover(self, root) -> int:
        self.countCameras = 0
        root_state = self.minCameraCoverUtil(root)

        if root_state == -1: # if root itself need camera
            self.countCameras += 1
        
        return self.countCameras