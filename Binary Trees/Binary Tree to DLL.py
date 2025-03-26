class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


#Function to convert a binary tree to doubly linked list.
class Solution:
    def bToDLLUtil(self, root):
        if root:
            self.bToDLLUtil(root.left)

            if self.foundHead == False:
                self.head = root
                self.prevNode = root

                self.foundHead = True
            
            else:
                self.prevNode.right = root
                root.left = self.prevNode
                self.prevNode = root

            self.bToDLLUtil(root.right)


    def bToDLL(self, root):
        self.head = None
        self.foundHead = False
        
        self.bToDLLUtil(root)

        return self.head

    
    def view(self, root):
        ptr = root

        while ptr:
            print(ptr.data, end=' ')
            ptr = ptr.right
        

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)

    sol = Solution()
    new_root = sol.bToDLL(root)
    sol.view(new_root)