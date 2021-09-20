class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def treeFromString(self, string):
        if len(string) == 0:
            return None
        
        self.root = string[0]
        self.string = string
        self.index = 0
        self.buildUpdatedString()
    
    def buildUpdatedString(self):
        if self.string[self.index].isdigit():
            node = Node(int(self.string[self.index]))

        
        
        
        