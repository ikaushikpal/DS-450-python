
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


#Function to return a tree created from postorder and inoreder traversals.

def constructBinaryTree(inOrder, postOrder, post_start, post_end, in_start, in_end):
    if post_start > post_end: # if left node is NULL
        return None
    
    if post_start == post_end:
        return Node(postOrder[post_end])

    root = Node(postOrder[post_end])
    pivot = in_start

    while pivot <= in_end and inOrder[pivot] != postOrder[post_end]:
        pivot += 1

    left_nodes = pivot - in_start

    root.left = constructBinaryTree(inOrder,
                                    postOrder,
                                    post_start,
                                    post_start+left_nodes-1,
                                    in_start,
                                    in_start+left_nodes-1)

    root.right = constructBinaryTree(inOrder,
                                    postOrder, 
                                    post_start+left_nodes, 
                                    post_end-1,
                                    in_start+left_nodes+1, 
                                    in_end)

    return root


def buildTree(inOrder, postOrder, n):
    return constructBinaryTree(inOrder, postOrder, 0, n-1, 0, n-1)

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
    N = 8
    inOrder = [4, 8, 2, 5, 1, 6, 3, 7]
    postOrder = [8, 4, 5, 2, 6, 7, 3, 1]

    root = buildTree(inOrder, postOrder, N)

    preorder(root)
    print()
    postorder(root)
    # Output: 1 2 4 8 5 3 6 7
    # Explanation: For the given postorder and
    # inorder traversal of tree the  resultant
    # binary tree will be
    #         1
    #     /      \
    #   2         3
    # /  \      /  \
    # 4    5    6    7
    # \
    #  8