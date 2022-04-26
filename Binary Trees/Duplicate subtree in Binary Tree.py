# Given a binary tree, find out whether it contains a duplicate sub-tree of size two or more, or not.

# Example 1 :
# Input : 
#                1
#              /   \ 
#            2       3
#          /   \       \    
#         4     5       2     
#                      /  \    
#                     4    5
# Output : 1
# Explanation : 
#     2     
#   /   \    
#  4     5
# is the duplicate sub-tree.


# Example 2 :
# Input : 
#                1
#              /   \ 
#            2       3
# Output: 0
# Explanation: There is no duplicate sub-tree 
# in the given binary tree.

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
        
    def dupSubUtil(self, root):
        if root is None:
            return '#'
        
        if self.containsDuplicate == True:
            return '#'
        
        s = '$' + str(root.data)    
        s += self.dupSubUtil(root.left)
        s += self.dupSubUtil(root.right)

        if root.left is None and root.right is None:
            return s

        if s in self.storedAddress:
            if self.storedAddress[s] >= 1:
                self.containsDuplicate = True
            self.storedAddress[s] += 1
        else:
            self.storedAddress[s] = 1
            
        return s

    def dupSub(self, root):
        self.containsDuplicate = False
        self.storedAddress = {}
        self.dupSubUtil(root)
        return int(self.containsDuplicate)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(2)
    root.right.right.left = Node(4)
    root.right.right.right = Node(5)
    print(Solution().dupSub(root))