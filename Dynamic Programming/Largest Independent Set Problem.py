# Given a Binary Tree, find size of the Largest Independent Set(LIS) in it. A subset of all tree nodes is an independent set if there is no edge between any two nodes of the subset. 

# For example, consider the following binary tree. The largest independent set(LIS) is {10, 40, 60, 70, 80} and size of the LIS is 5.



# A binary tree node has data,
#pointer to left child and a
#pointer to right child
class node :
    def __init__(self):
        self.data = 0
        self.left = self.right = None
 
# The function returns size of the
# largest independent set in a given
# binary tree
class Solution:
    def helper(self, root):
        if root is None:
            return 0

        if root in self.memo:
            return self.memo[root]

        exclude = self.helper(root.left) + self.helper(root.right)

        include = 1
        if root.left:
            include += self.helper(root.left.left) + self.helper(root.left.right)

        if root.right:
            include += self.helper(root.right.left) + self.helper(root.right.right)

        self.memo[root] = max(include, exclude)
        return self.memo[root]

    def largestIndependentSet(self, root):
        # Base case
        self.memo = {}
        return self.helper(root)

        
# A utility function to create a node
def newNode( data ) :
    temp = node()
    temp.data = data
    temp.left = temp.right = None
    return temp
 
# Driver Code
 
# Let us construct the tree
# given in the above diagram
root = newNode(20)
root.left = newNode(8)
root.left.left = newNode(4)
root.left.right = newNode(12)
root.left.right.left = newNode(10)
root.left.right.right = newNode(14)
root.right = newNode(22)
root.right.right = newNode(25)


sol = Solution()
print(sol.largestIndependentSet(root))