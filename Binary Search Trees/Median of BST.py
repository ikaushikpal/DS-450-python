# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

import math


def count(root):
    if root is None: return 0

    return count(root.left) + count(root.right) + 1

def kthSmallest(root, k):
    if root is None:
        return None
    
    left = kthSmallest(root.left, k)
    if left:
        return left

    k[0] -= 1
    if k[0] == 0:
        return root

    right = kthSmallest(root.right, k)
    if right:
        return right
    
    return None

def findMedian(root):
    # code here
    # return the median
    noNodes = count(root)

    if noNodes % 2 == 1: # odd  no of nodes
        k = (noNodes+1) // 2
        return kthSmallest(root, [k]).data
        
    else:
        k1 = noNodes // 2
        k2 = math.ceil((noNodes+1) / 2)
        
        res = (kthSmallest(root, [k1]).data + kthSmallest(root, [k2]).data) / 2
        
        if res.is_integer():
            return int(res)
        else:
            return res
