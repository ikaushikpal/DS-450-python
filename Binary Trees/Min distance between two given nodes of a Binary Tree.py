
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def findNodeToRoot(self, root, targetVal:int)->list:
        if root is None: # base case
            return []

        if root.data == targetVal: # if we found the node
            return [root.data]
        

        left = self.findNodeToRoot(root.left, targetVal)
        if len(left) > 0: # checking if we found targetNode in left branch
            # we are checking only length because if len > 0 meaning we found node
            left.append(root.data)
            return left

        # if we did not found targetNode in left then proceed to right branch

        right = self.findNodeToRoot(root.right, targetVal)
        if len(right) > 0: # checking if we found targetNode in right branch
            right.append(root.data)
            return right

        return [] # we did not found targetNode in this subTree


    def findDist(self, root, val1:int, val2:int)->int:
        #return: minimum distance between val1 and val2 in a tree with given root
        
        val1_path = self.findNodeToRoot(root, val1)
        if len(val1_path) == 0: # meaing we val1 doesn't exist in tree first place
            return -1

        val2_path = self.findNodeToRoot(root, val2)
        if len(val2_path) == 0: # meaing we val2 doesn't exist in tree first place
            return -1

        # same code for finding LCA(Lowest Common Ancestor) between two nodes in BT
        m, n = len(val1_path), len(val2_path)
        i, j = m-1, n-1

        while i>=0 and j>=0 and val1_path[i] == val2_path[j]:
            i -= 1
            j -= 1

        # and val1 and val2 are 70 and 110 respectively
        # lets say val1_path = [70, 30, 10]
        # and val2_path = [110, 80, 30, 10]
        # after loop i will be 0 and j be 1
        # this is the postion where val1 and val2 disverge their paths
        # incrementing i and j will point LCA which is 30
        i += 1
        j += 1
        # if we only to find LCA then return val1_path[i] or val2_path[j]
        # ==========================================================================

        # why cost 
        # Now i and j will point to LCA
        #  for our example min_dist between 70 and 110 is 3
        # i = 1 and j = 2; So i+j = 3 which is our min_dist 
        cost = i + j

        return cost