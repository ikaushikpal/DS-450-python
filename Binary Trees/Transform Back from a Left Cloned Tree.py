class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None


class Solution:
    def transformNormal(self, root):
        if root is None:
            return None

        if root.left:
            root.left = root.left.left

        self.transformNormal(root.left)
        self.transformNormal(root.right)

        return root


def preOrder(root):
    if root:
        print(root.data, end=' ')

        preOrder(root.left)
        preOrder(root.right)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(10)
    root.left.left = Node(20)
    root.left.left.left = Node(20)
    root.right = Node(30)
    root.right.left = Node(30)

    preOrder(root)
    print()
    root = Solution().transformNormal(root)

    preOrder(root)