class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def minValue(root):
    if root is None:
        return float('inf')
    
    return min(root.data, minValue(root.left))

def insert(node, data):
    if node is None:
        return (Node(data))
 
    else:
        # 2. Otherwise, recur down the tree
        if data <= node.data:
            node.left = insert(node.left, data)
        else:
            node.right = insert(node.right, data)
 
        # Return the (unchanged) node pointer
        return node


if __name__ == '__main__':
    root = None
    root = insert(root,4)
    insert(root,2)
    insert(root,1)
    insert(root,3)
    insert(root,6)
    insert(root,5)

    print(minValue(root))