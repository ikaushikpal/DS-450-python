# Given a linked list of N nodes, sorted in ascending order based on the absolute values of its data,i.e. negative values are considered as positive ones. Sort the linked list in ascending order according to the actual values, and consider negative numbers as negative and positive numbers as positive.


# Example 1:
# Input: 
# List: 1, -2, -3, 4, -5
# Output: 
# List: -5, -3, -2, 1, 4
# Explanation: 
# Actual sorted order of {1, -2, -3, 4, -5}
# is {-5, -3, -2, 1, 4}
 

# Example 2:
# Input: 
# List: 5, -10
# Output: 
# List: -10, 5
# Explanation:
# Actual sorted order of {5, -10}
# is {-10, 5}


class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def split(self, head):
        positiveHead = positiveTail = Node(None)
        negativeHead = negativeTail = Node(None)
        
        ptr = head
        while ptr:
            if ptr.data < 0:
                negativeTail.next = ptr
                negativeTail = ptr
            else:
                positiveTail.next = ptr
                positiveTail = ptr
            ptr = ptr.next
        
        positiveTail.next = None
        negativeTail.next = None
        return positiveHead.next, negativeHead.next
    
    def reverse(self, head):
        prevNode = currNode = None
        nextNode = head
        
        while nextNode:
            prevNode = currNode
            currNode = nextNode
            nextNode = nextNode.next
            
            currNode.next = prevNode
        return currNode
        
    def sortList(self,head):
        pos, neg = self.split(head)
        negRev = self.reverse(neg)
        
        if neg:
            neg.next = pos
            return negRev
        return pos
# Time Complexity: O(n)
# Space Complexity: O(1)