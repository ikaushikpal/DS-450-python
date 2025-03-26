# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.


# Example 1:

# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

# Example 2:

# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]

# Example 3:

# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]


from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        # approach:
        # 1. create a new linked list with the same structure as the original one
        # 2. while iterating through the original linked list, make copiedNode.random = originalNode and originalNode.next = copiedNode
        # 3. after making the copiedNode.random, iterate through the original linked list again
        # 4. Now set copiedNode.random = originalNode.random.random.next

        if not head:
            return None

        # coping original ll
        newHead = None
        prevPtr, ptr = None, head
        newPtr = newHead
        
        while ptr:
            prevPtr = ptr
            ptr = ptr.next
            node = Node(prevPtr.val)
            
            if not newHead:
                newHead = newPtr = node
            else:
                newPtr.next = node
                newPtr = node
                
            prevPtr.next = newPtr
            newPtr.random = prevPtr
            
        newPtr = newHead
        while newPtr:
            ptr = newPtr.random
            newPtr.random = ptr.random.next if ptr.random else None
            ptr.next = newPtr.next.random if newPtr.next else None
            newPtr = newPtr.next
            
        return newHead
                

a = Node(7)
b = Node(13)
c = Node(11)
d = Node(10)
e = Node(1)

a.next = b
b.next = c
c.next = d
d.next = e

a.random = None
b.random = a
c.random = e
d.random = c
e.random = a

sol = Solution()
print(sol.copyRandomList(a))