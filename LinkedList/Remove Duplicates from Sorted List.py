# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
    def deleteDuplicates(self, root):
        if root is None:
            return None

        newRoot  = currentNewPtr = None
        currentOldPtr = nextOldPtr = root

        while nextOldPtr and currentOldPtr:

            while nextOldPtr and nextOldPtr.val == currentOldPtr.val:
                nextOldPtr = nextOldPtr.next
            
            if currentNewPtr is None:
                newRoot = currentNewPtr = currentOldPtr
            else:
                currentNewPtr.next = currentOldPtr
                currentNewPtr =  currentOldPtr

            currentOldPtr = nextOldPtr
        
        if currentNewPtr:
            currentNewPtr.next = None

        return newRoot