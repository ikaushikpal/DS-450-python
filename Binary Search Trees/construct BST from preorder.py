class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# copied from construct binary tree from preorder and inorder
class Solution:

    def constructTree(self, pre_start_index, pre_end_index, in_start_index, in_end_index):
        if pre_start_index > pre_end_index: # or in_start_index > in_end_index
            return None # why none it will trigger when left child is NULL

        if pre_start_index == pre_end_index: # or in_start_index==in_end_index
            return Node(self.preOrder[pre_start_index]) # leaf node

        root = Node(self.preOrder[pre_start_index])

        index = in_start_index
        while index <= in_end_index and self.preOrder[pre_start_index] != self.inOrder[index]:
            index += 1

        left_nodes = index - in_start_index
        # count of nodes which are in leaf sub tree

        root.left = self.constructTree(pre_start_index+1, pre_start_index+left_nodes, in_start_index, index-1)
        root.right = self.constructTree(pre_start_index+left_nodes+1, pre_end_index, index+1, in_end_index)

        return root


    def buildtree(self, inorder, preorder, n):
        # code here
        # build tree and return root Node
        self.inOrder = inorder
        self.preOrder = preorder

        return self.constructTree(0, n-1, 0, n-1)
#========================================================

def constructTree(preorder, size): # to construct BST from preorder
    inorder = preorder.copy()
    inorder.sort() # in case of a BST its inorder is sorted in ascending order
    # O(nlogn)

    return Solution().buildtree(inorder, preorder, size)

    # time complexity = O(nlogn)
    # space complexity = O(n)
    
# utility==================================================
def preorder(root):
    if root:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ')


if __name__ == '__main__':
    pre = [10, 5, 1, 7, 40, 50]
    root = constructTree(pre, len(pre))
    
    preorder(root)
    print()
    postorder(root)