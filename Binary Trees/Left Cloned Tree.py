class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None


class Solution:
    def transformLeftCloned(self, root):
        if root is None:
            return None

        newNode = Node(root.data)
        newNode.left = root.left
        root.left = newNode

        self.transformLeftCloned(newNode.left)
        self.transformLeftCloned(root.right)

        return root


def preOrder(root):
    if root:
        print(root.data, end=' ')

        preOrder(root.left)
        preOrder(root.right)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)

    root = Solution().transformLeftCloned(root)

    preOrder(root)

