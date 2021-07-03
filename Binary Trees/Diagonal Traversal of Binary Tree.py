# https://practice.geeksforgeeks.org/problems/diagonal-traversal-of-binary-tree/1

from collections import defaultdict

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#:param root: root of the given tree.
#return: print out the diagonal traversal,  no need to print new line
maxDiagonal = 0

def diagonal(root):
    global maxDiagonal
    maxDiagonal = 0

    hashMap = defaultdict(list)
    diagonalUtil(root, 0, hashMap)
    
    res = []
    
    for i in range(maxDiagonal+1):
        res.extend(hashMap[i])
    
    return res

def diagonalUtil(root, index, hashMap):
    if root is None:
        return
    global maxDiagonal

    hashMap[index].append(root.data)
    maxDiagonal = max(maxDiagonal, index)

    diagonalUtil(root.left, index+1, hashMap)
    diagonalUtil(root.right, index, hashMap)
