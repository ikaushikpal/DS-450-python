class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def constructBSTInorder_util(self, inorder, low, high):
        if low > high:
            return None
        
        mid = (low + high) // 2
        root = Node(inorder[mid])

        root.left = self.constructBSTInorder_util(inorder, low, mid-1)
        root.right = self.constructBSTInorder_util(inorder, mid+1, high)

        return root


    def constructBSTInorder(self, inorder, size):
        return self.constructBSTInorder_util(inorder, 0, size-1)


def preorder(root):
    if root:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)


if __name__ == '__main__':
    inodr = [9, 12, 14, 17, 19, 23, 50, 54 ,67, 72, 76]

    root = Solution().constructBSTInorder(inodr, len(inodr))
    preorder(root)
    print()
    inorder(root)
