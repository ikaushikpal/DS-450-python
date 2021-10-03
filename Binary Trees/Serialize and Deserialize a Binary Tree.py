class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


class Solution:

    def serialize(self, root, storedList):
        if root is None:
            storedList.append(-1)
            return storedList
        
        storedList.append(root.data)
        self.serialize(root.left, storedList)
        self.serialize(root.right, storedList)

        return storedList
    

    def deSerializeUtil(self):
        if self.index == len(self.storedList):
            return


        if self.storedList[self.index] == -1:
            self.index += 1
            return None

        root = Node(self.storedList[self.index])
        self.index += 1
        root.left = self.deSerializeUtil()
        root.right = self.deSerializeUtil()

        return root

    def deSerialize(self, storedList):
        self.storedList = storedList
        self.index = 0
        return self.deSerializeUtil()

#Function to serialize a tree and return a list containing nodes of tree.
def serialize(root, storedList):
    #code here
    return Solution().serialize(root, storedList)

#Function to deserialize a list and construct the tree.   
def deSerialize(storedList):
    #code here
    return Solution().deSerialize(storedList)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
A= []

serialize(root, A)
deSerialize(A)