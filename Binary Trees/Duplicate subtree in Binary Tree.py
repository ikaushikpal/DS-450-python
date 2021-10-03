class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None



class Solution:
        
    def dupSubUtil(self, root):
        if root is None:
            return '$'
        
        if not root.left and not root.right:
            return str(root.data) 
            
        s = str(root.data)    
        s += self.dupSubUtil(root.left)
        s += self.dupSubUtil(root.right)
        
        if s in self.storedAddress:
            self.storedAddress[s] += 1
        else:
            self.storedAddress[s] = 1
            
        return s

    def dupSub(self, root):
        self.storedAddress = {}
        self.dupSubUtil(root)

        for val in self.storedAddress.values():
            if val >= 2:
                return 1
        
        return 0