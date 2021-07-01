class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def inorder(root):
	if root is None:
		return

	inorder(root.left)
	print(root.data, end = " ")
	inorder(root.right)


def mirrorBT(root):
    if root is None:
        return None
    
    left = mirrorBT(root.left)
    right = mirrorBT(root.right)

    root.left = right
    root.right = left

    return root

if __name__=='__main__':

	tree = Node(5)
	tree.left = Node(3)
	tree.right = Node(6)
	tree.left.left = Node(2)
	tree.left.right = Node(4)

	print("Inorder of original tree: ")
	inorder(tree)

	mirror = mirrorBT(tree)

	print("\nInorder of mirror tree: ")
	inorder(mirror)