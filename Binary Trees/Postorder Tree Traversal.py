from collections import deque


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"{self.data}"
    
def postOrderRecursive(root):
    if root:
        postOrderRecursive(root.left)
        postOrderRecursive(root.right)
        print(f'{root.data}', end=' ')
 

def postOrderIterativeTwoStacks(root):
    stack1 = deque()
    stack2 = deque()

    stack1.append(root)

    while len(stack1):
        currentNode = stack1.pop()
        stack2.append(currentNode)

        if currentNode.left:
            stack1.append(currentNode.left)
        
        if currentNode.right:
            stack1.append(currentNode.right)

    while len(stack2):
        topElement = stack2.pop()
        print(topElement.data, end=' ')
    
def postOrderIterativeOneStack(root):
    currentNode = root
    stack = deque()

    while currentNode or  len(stack):
        if currentNode:
            stack.append(currentNode)
            currentNode = currentNode.left
        else:
            topElement = stack[-1]

            if topElement != None:
                topElement = stack.pop()
                print(topElement.data, end=' ')

                if topElement == stack[-1].right:
                    print(stack.pop().data, end=' ')
                else:
                    currentNode = stack[-1]
                        
                while len(stack) and topElement == stack[-1]:
                    topElement = stack.pop()
                    print(topElement.data, end=' ')

                
            else:
                currentNode = topElement


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    postOrderRecursive(root)
    print()
    print("=" * 35)

    postOrderIterativeTwoStacks(root)
    print()
    print("=" * 35)

    postOrderIterativeOneStack(root)
    print()
    print("=" * 35)