from collections import deque


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def __repr__(self):
        return self.data
    
def inOrderRecursive(root):
    if root:
        inOrderRecursive(root.left)
        print(f'{root.data}', end=' ')
        inOrderRecursive(root.right)
 
def inOrderIterative(root):
    stack = deque()
    current = root
    
    while len(stack) or current:
        while current:
            stack.append(current)
            current = current.left
        
        topElement = stack.pop()

        if current is None:
            print(topElement.data, end=' ')
            current = topElement.right



if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    inOrderRecursive(root)
    print()
    print("=" * 35)

    inOrderIterative(root)
    print()
    print("=" * 35)