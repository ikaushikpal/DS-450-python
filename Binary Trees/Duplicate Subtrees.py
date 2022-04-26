# Given a binary tree of size N, your task is to that find all duplicate subtrees from the given binary tree.


# Example:
# Input : 
# Output : 2 4
#          4
# Explanation: Above Trees are two 
# duplicate subtrees.i.e  and 
# Therefore,you need to return above trees 
# root in the form of a list.

class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

    def __str__(self):
        return self.data
    
    def __repr__(self) -> str:
        return self.__str__()


class Solution:
    def dfs(self, root):
        if root is None:
            return '#'
        
        pattern = '$' + str(root.data) + self.dfs(root.left) + self.dfs(root.right) + '#'
        self.addPattern(pattern, root)
        return pattern
    
    
    def addPattern(self, pattern, root):
        if pattern in self.patterns and self.patterns[pattern] == 1:
            self.dups.append(root)
            
        if pattern not in self.patterns:
            self.patterns[pattern] = 1
        else:
            self.patterns[pattern] += 1

    def printAllDups(self, root):
        if root is None:
            return []

        self.patterns = {}
        self.dups = []
        self.dfs(root)
        return self.dups


if __name__ == '__main__':
    # 2 1 11 11 N 1
    root = Node(2)
    root.left = Node(1)
    root.right = Node(11)
    root.left.left = Node(11)
    root.right.left = Node(1)

    print(Solution().printAllDups(root))

    root = Node(1)
    root.left = Node(0)
    root.right = Node(0)
    root.left.left = Node(0)
    root.left.right = Node(0)

    root.left.left.left = Node(0)
    root.left.left.right = Node(0)

    root.left.right.left = Node(0)
    root.left.right.right = Node(0)

    root.left.left.left.left = Node(0)
    print(Solution().printAllDups(root))
