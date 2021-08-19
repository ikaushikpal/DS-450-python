# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
    def rotateRight(self, root, k):
        if not root or not root.next or not k:
            return root
            
        prevNode = None
        currentNode = root
        count = 0

        while currentNode:
            prevNode = currentNode
            currentNode = currentNode.next
            count += 1
        
        #end node = prev
        prevNode.next = root # making circular linkedlist

        travel = count - (k%count)
        count = 0
        prevNode = None
        currentNode = root

        while count < travel:
            prevNode = currentNode
            currentNode = currentNode.next
            count += 1
        
        prevNode.next = None
        return currentNode