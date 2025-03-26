# Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:
# (i) a next pointer to the next node,
# (ii) a bottom pointer to a linked list where this node is head.
# Each of the sub-linked-list is in sorted order.
# Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. 
# Note: The flattened list will be printed using the bottom pointer instead of next pointer.

 

# Example 1:

# Input:
# 5 -> 10 -> 19 -> 28
# |     |     |     | 
# 7     20    22   35
# |           |     | 
# 8          50    40
# |                 | 
# 30               45
# Output:  5-> 7-> 8- > 10 -> 19-> 20->
# 22-> 28-> 30-> 35-> 40-> 45-> 50.
# Explanation:
# The resultant linked lists has every 
# node in a single level.
# (Note: | represents the bottom pointer.)
 

# Example 2:

# Input:
# 5 -> 10 -> 19 -> 28
# |          |                
# 7          22   
# |          |                 
# 8          50 
# |                           
# 30              
# Output: 5->7->8->10->19->22->28->30->50
# Explanation:
# The resultant linked lists has every
# node in a single level.

# (Note: | represents the bottom pointer.)


import heapq


class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None


class Solution:
    def createMinHeap(self, head, minHeap):
        counter = 0
        ptr = head
        
        while ptr:
            minHeap.append((ptr.data, counter, ptr))
            
            nextPtr = ptr.next
            ptr.next = None
            ptr = nextPtr
            
            counter += 1
            
        heapq.heapify(minHeap)
        return counter
    
    def flatten(self,root):
        minHeap = []
        counter = self.createMinHeap(root, minHeap)
        newHead = newTail = Node(None)
        
        while minHeap:
            _, _ , node = heapq.heappop(minHeap)
            bottomNode = node.bottom
            
            newTail.bottom = node
            newTail = node
            node.bottom = None
            
            if bottomNode:
                heapq.heappush(minHeap, (bottomNode.data, counter, bottomNode))
                counter += 1
        return newHead.bottom
# Time Compexity: O(nlogn)
# Space Complexity: O(n)