import heapq


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

    # =================================================

    def storeInorder(self, root, inOrder):
        if root:
            self.storeInorder(root.left, inOrder)
            inOrder.append(root.data)
            self.storeInorder(root.right, inOrder)
            return inOrder

    def mergeTwoBST(self, root1, root2):
        # edge cases ======================
        if root1 is None and root2:
            return root2
        
        if root1 and not root2:
            return root1

        if not root1 and not root2:
            return None
        # =================================

        root1_inorder = self.storeInorder(root1, [])
        root2_inorder = self.storeInorder(root2, [])

        # merge two arrays
        new_inorder = list(heapq.merge(root1_inorder, root2_inorder, key=lambda x: x))

        # built tree 
        return self.constructBSTInorder(new_inorder, len(new_inorder))

# utility ============================================

def insert(root, data):
    if not root:
        return Node(data)
    if root.data == data:
        return root
    elif root.data > data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

def printAll(root):
    print("PreOrder")
    preorder(root)

    print("\nInOrder")
    inorder(root)

    print("\nPostOrder")
    postorder(root)
    print()
    print('=' * 50)

def preorder(root):
    if root is None:
        return

    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)

def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data, end=' ')
# =====================================================
if __name__ == '__main__':
    root1 = root2 = None

    root1 = insert(root1, 100)
    root1 = insert(root1, 50)
    root1 = insert(root1, 300)
    root1 = insert(root1, 20)
    root1 = insert(root1, 70)
    printAll(root1) 
    
    root2 = insert(root2, 80)
    root2 = insert(root2, 40)
    root2 = insert(root2, 120)
    printAll(root2)

    root3 = Solution().mergeTwoBST(root1, root2)
    printAll(root3) 