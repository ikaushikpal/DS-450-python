# Given the array representation of Complete Binary Tree i.e, if index i is the parent, index 2*i + 1 is the left child and index 2*i + 2 is the right child. The task is to find the minimum number of swap required to convert it into Binary Search Tree.

# Examples:  

# Input : arr[] = { 5, 6, 7, 8, 9, 10, 11 }
# Output : 3
# Binary tree of the given array:
# dig11

# Swap 1: Swap node 8 with node 5.
# Swap 2: Swap node 9 with node 10.
# Swap 3: Swap node 10 with node 7.
# dig21

# So, minimum 3 swaps are required.


# Input : arr[] = { 1, 2, 3 }
# Output : 1
# Binary tree of the given array:
# dig3

# After swapping node 1 with node 2.
# dig41

# So, only 1 swap required.


# NOTE:
# this problem is exactly same as the problem of finding the minimum number of swaps required to sort the array.

# find inorder traversal of the tree along with the index of the node from 0
# and then run algo