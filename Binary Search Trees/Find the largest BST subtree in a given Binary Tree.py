class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class NodeInfo:

    def __init__(self,
                minVal=float('inf'),
                maxVal=float('-inf'),
                isBst=True,
                root=None,
                size=0):

        self.min = minVal
        self.max = maxVal
        self.isBST = isBst
        self.head = root
        self.size = size


class Solution:
    def largestBst_util(self, root)->NodeInfo:
        if root is None:
            return NodeInfo()
        
        left = self.largestBst_util(root.left)
        right = self.largestBst_util(root.right)

        currentNodeInfo = NodeInfo()

        # setting min first
        currentNodeInfo.min = min(root.data, left.min, right.min)

        # max 
        currentNodeInfo.max = max(root.data, left.max, right.max)

        # checking whether is current node is a BST
        # first checking if left sub tree and right sub tree is BST first
        # because if left or right anyone of them is not BST then current root cannot be a BST

        isCapable = left.isBST & right.isBST

        if isCapable == True: #meaing left and right subtree both BST
            # now check if current node is BST

            currentNodeInfo.isBST = root.data > left.max and root.data < right.min # No duplicates allowed

        else:
            currentNodeInfo.isBST = False


        # now finding maximum size BST subtree among left  right and current

        if currentNodeInfo.isBST == True: # if current node is BST then only it is capable of beeing root
            currentNodeInfo.head = root
            currentNodeInfo.size = left.size + right.size + 1
        
        elif left.size > right.size:
            currentNodeInfo.head = left.head
            currentNodeInfo.size = left.size

        else:
            currentNodeInfo.head = right.head
            currentNodeInfo.size = right.size

        return currentNodeInfo
        

    # Return the size of the largest sub-tree which is also a BST
    def largestBst(self, root):
        treeInfo = self.largestBst_util(root)
        return treeInfo.size

if __name__ == '__main__':
    root = Node(5)
    root.left = Node(2)
    root.right = Node(4)
    root.left.left = Node(1)
    root.left.right = Node(3)


    s = Solution()
    print(s.largestBst(root))