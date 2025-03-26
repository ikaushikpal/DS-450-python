# Node class
class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None


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
    


if __name__ == '__main__':
    preorder = ['A', 'B', 'D', 'E', 'C', 'F']
    inorder = ['D', 'B', 'E', 'A', 'C', 'F']

    Solution().buildtree(inorder, preorder, len(preorder))
