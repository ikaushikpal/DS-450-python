class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = self.right = None

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def morrisInOrder(self, root):
        if root is None:
            return None
        
        inOrder = []
        currentNode = root

        while currentNode:
            # case 1
            if currentNode.left is None:
                inOrder.append(currentNode.val)
                # go right
                currentNode = currentNode.right

            # case 2
            else:
                prevNode = currentNode.left
                while prevNode.right and prevNode.right != currentNode:
                    prevNode = prevNode.right
                
                # creating thread
                if prevNode.right is None:
                    prevNode.right = currentNode
                    # go left
                    currentNode = currentNode.left
                
                # deleting thread
                else:
                    prevNode.right = None
                    inOrder.append(currentNode.val)
                    # go right
                    currentNode = currentNode.right
        return inOrder
# Time Complexity : O(N)
# Space Complexity : O(1)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    sol = Solution()
    print(sol.morrisInOrder(root))