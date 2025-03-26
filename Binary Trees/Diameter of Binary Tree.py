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
    
    
    def diameterGfg(self, root):
        height = Height()
        return self.diameterOpt(root, height)
    
    def diameter(self, root):
        self.res = -10**9
        self.diameterUtil(root)
        return self.res

    def diameterUtil(self, root):
        if root is None:
            return 0
        # if root is null ptr then return 0

        leftDiameter = self.diameterUtil(root.left)  # leftDiameter is nothing but left height 
        rightDiameter = self.diameterUtil(root.right)# rightDiameter is nothing but right height 

        temp = max(leftDiameter, rightDiameter) + 1
        # if current root is not root for maximum path

        ans = max(temp, 1+leftDiameter+rightDiameter)
        # 1+leftDiameter+rightDiameter will give value if current root is the main root of path
        # ans will give is current root is main root of path
        # if it is then ans = 1+left+right but if no then ans = temp (just another node in path)

        self.res = max(self.res , ans) #updating res for maximum path

        return temp # returning current height
