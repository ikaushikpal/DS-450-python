class Height:
    def __init(self):
        self.h = 0
        
        
class Solution:
    def diameterOpt(self, root, height):
        lh = Height()
        rh = Height()

        if root is None:
            height.h = 0
            return 0

        ldiameter = self.diameterOpt(root.left, lh)
        rdiameter = self.diameterOpt(root.right, rh)
    
        height.h = max(lh.h, rh.h) + 1
        return max(lh.h + rh.h + 1, max(ldiameter, rdiameter))
    
    
    def diameter(self, root):
        height = Height()
        return self.diameterOpt(root, height)
