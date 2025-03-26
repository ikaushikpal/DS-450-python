# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def storeData(self, root, myDict):
        if root:
            self.storeData(root.left, myDict)
            self.myDict[root.data] = True
            self.storeData(root.right, myDict)

    def countPairs(self, root1, root2, x) -> int: 
        root1Dict = {}
        root2Dict  = {}

        self.storeData(root1, root1Dict)
        self.storeData(root2, root2Dict)

        count = 0
        for key in root1Dict.keys():
            if x-key in root2Dict:
                count += 1
        
        return count