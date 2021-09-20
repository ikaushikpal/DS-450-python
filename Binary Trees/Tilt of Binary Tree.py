class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    def tiltOfBinaryTreeUtil(self, root):
        if root is None:
            return 0
        
        left_tilt = self.tiltOfBinaryTreeUtil(root.left)
        right_tilt = self.tiltOfBinaryTreeUtil(root.right)

        currentNode_tilt = abs(left_tilt - right_tilt)
        self.total_tilt += currentNode_tilt

        return root.data + left_tilt + right_tilt


    def tiltOfBinaryTree(self, root):
        self.total_tilt = 0
        self.tiltOfBinaryTreeUtil(root)

        return self.total_tilt



if __name__ == '__main__':
    root = Node(50)
    root.left = Node(10)
    root.right = Node(40)
    root.left.left = Node(30)
    root.left.right = Node(20)

    print(Solution().tiltOfBinaryTree(root))

    #     4
    #    / \
    #   2   9
    #  / \   \
    # 3   5   7

    # Explanation: 
    # Tilt of node 3 : 0
    # Tilt of node 5 : 0
    # Tilt of node 7 : 0
    # Tilt of node 2 : |3-5| = 2
    # Tilt of node 9 : |0-7| = 7
    # Tilt of node 4 : |(3+5+2)-(9+7)| = 6
    # Tilt of binary tree : 0 + 0 + 0 + 2 + 7 + 6 = 15
    
    root = Node(4)
    root.left = Node(2)
    root.right = Node(9)
    root.right.right = Node(7)
    root.left.left = Node(3)
    root.left.right = Node(5)

    print(Solution().tiltOfBinaryTree(root))

