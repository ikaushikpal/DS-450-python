# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
    def countNodes(self, root):
        counter = 0
        ptr = root
        while ptr:
            counter += 1
            ptr = ptr.next
        return counter


    def removeNthFromEnd(self, root, n):
        if root is None or n == 0:
            return root

        count = self.countNodes(root)
        if count <= n:
            return root.next
        
        prevNode, currNode = None, root
        for _ in range(count - n):
            prevNode = currNode
            currNode = currNode.next
        
        if currNode.next == None:
            prevNode.next = None
        
        else:
            prevNode.next = currNode.next
        
        return root
        

