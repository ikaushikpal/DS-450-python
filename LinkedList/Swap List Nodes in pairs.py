# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
    def swapPairs(self, A):
        return self.reverseList(A, 2) # easy recursive approach

    def reverseList(self, root, k):
        if k == 0:
            return root
            
        if not root or not root.next:
            return root
        
        prevNode = currentNode = None
        nextNode = root
        count = 0

        while nextNode and count < k:
            prevNode = currentNode
            currentNode = nextNode
            nextNode = nextNode.next

            currentNode.next = prevNode
            count += 1

        if nextNode:
            root.next = self.reverseList(nextNode, k)
        
        return currentNode

    def swapPairs(self, root):
        if not root or not root.next:
            return root
        
        prevNode = None
        currentNode = root
        count = 1

        while currentNode:
            if count%2==0:
                currentNode.val, prevNode.val = prevNode.val, currentNode.val

            prevNode = currentNode
            currentNode = currentNode.next
            count += 1
        
        return root