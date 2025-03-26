class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class Solution:
    def findPartision(self, inOrder, start, end, key):
        for i in range(start, end+1):
            if inOrder[i] == key:
                return i
    

    def createDictionary(self, inOrder, start, end):
        myDict = {}

        for i in range(start, end+1):
            key = inOrder[i]
            myDict[key] = True

        return myDict


    def builtLeftRightLevelOrder(self, levelOrder, level_start, level_end, inorder_dict):
        levelOrder_left = []
        levelOrder_right = []

        for i in range(level_start, level_end+1):
            key = levelOrder[i]

            if key in inorder_dict:
                levelOrder_left.append(key)
                del inorder_dict[key]
            
            else:
                levelOrder_right.append(key)

        return levelOrder_left, levelOrder_right


    def buildTreeUtil(self, levelOrder, inOrder, in_start, in_end):
        if len(levelOrder)==0 or in_start > in_end:
            return None

        level_start, level_end = 0, len(levelOrder)-1
        root_value = levelOrder[level_start] 

        # finding where to split
        index = self.findPartision(inOrder, in_start, in_end, root_value)

        # creating root node
        root = Node(root_value) 

        inorder_dict = self.createDictionary(inOrder, in_start, index-1)

        # spliting level order in to left and right for building left and right sub tree
        levelOrder_left, levelOrder_right = self.builtLeftRightLevelOrder(levelOrder, level_start+1, level_end, inorder_dict)

        root.left = self.buildTreeUtil(levelOrder_left, inOrder, in_start, index-1)
        root.right = self.buildTreeUtil(levelOrder_left, inOrder, index+1, in_end)

        return root


    def buildTree(self, levelOrder, inOrder):
        return self.buildTreeUtil(levelOrder, inOrder, 0, len(inOrder)-1)

def buildTree(level, ino):
    #code here
    #return root of tree
    return Solution().buildTree(level, ino)