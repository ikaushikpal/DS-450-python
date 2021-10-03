class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def treeFromString(self, string):
        if len(string) == 0:
            return None
        
        return self.builtTree(string, 0, len(string)-1)
        
    def findDigit(self, string, start, end):
        number = ''
        while start<=end and string[start] != '(' and string[start]!=')':
            number += string[start]
            start += 1
        
        return int(number), start
    
    def findPartison(self, string, start, end):
        count_left, count_right = 1, 0
        if string[start] == ')':
            return start
        
        while start <= end and count_left != count_right:
            if string[start] == '(' : count_left += 1
            elif string[start] == ')' : count_right += 1

            start += 1
        
        return start

    def builtTree(self, string, start, end):
        if start > end:
            return None

        number, left_index = self.findDigit(string, start, end)
        root = Node(number)

        if left_index <= end:
            pivot = self.findPartison(string, left_index+1, end)

            root.left =  self.builtTree(string, left_index+1, pivot-2)
            root.right = self.builtTree(string, pivot+1, end-1)
            
        return root

# utility ============================================
def printAll(root):
    print("PreOrder")
    preorder(root)

    print("\nInOrder")
    inorder(root)

    print("\nPostOrder")
    postorder(root)
    print()
    print('=' * 50)

def preorder(root):
    if root is None:
        return

    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)

def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data, end=' ')
# =====================================================
if __name__ == '__main__':    
# Input : "1(2)(3)" 
# Output : 1 2 3
# Explanation :
#            1
#           / \
#          2   3
# Explanation: first pair of parenthesis contains 
# left subtree and second one contains the right 
# subtree. Preorder of above tree is "1 2 3".  
    root = Solution().treeFromString("1(2)(3)")
    printAll(root)  
    
# Input : "4(2(3)(1))(6(5))"
# Output : 4 2 3 1 6 5
# Explanation :
#            4
#          /   \
#         2     6
#        / \   / 
#       3   1 5   
    root = Solution().treeFromString("4(2(3)(1))(6(5))")
    printAll(root) 