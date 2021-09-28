class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Info:
    def __init__(self, root=None, count=1):
        self.root = root
        self.count = count


class Info:
    def __init__(self, root=None, count=1):
        self.root = root
        self.count = count


class Solution:
    def update(self, s, root):
        if s in self.storedAddress:
            self.storedAddress[s].count += 1
        else:
            self.storedAddress[s] = Info(root, 1)
            
    def dupSubUtil(self, root):
        if root is None:
            return '$'
        
        s = f"!{str(root.val)}{self.dupSubUtil(root.left)}{self.dupSubUtil(root.right)}!"       
        self.update(s, root)
            
        return s

    def findDuplicateSubtrees(self, root):
        self.storedAddress = {}
        self.dupSubUtil(root)

        return [val.root for val in self.storedAddress.values() if val.count>1]



if __name__ == '__main__':
    # 2 1 11 11 N 1
    root = Node(2)
    root.left = Node(1)
    root.right = Node(11)
    root.left.left = Node(11)
    root.right.left = Node(1)

    print(Solution().printAllDups(root))
