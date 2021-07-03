class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def treeFromString(self, string):
        if len(string) == 0:
            return None
        
        root = string[0]
        self.newString = []
        self.buildUpdatedString(string, 1)
    
    def buildUpdatedString(self, string, index):
        if index == len(string):
            return
        
        