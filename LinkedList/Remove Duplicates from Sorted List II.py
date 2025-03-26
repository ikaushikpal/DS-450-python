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

        newRoot = prevNewPtr = currentNewPtr = None
        prevOldPtr  = currentOldPtr = nextOldPtr = root

        while nextOldPtr and currentOldPtr:

            while nextOldPtr and nextOldPtr.val == currentOldPtr.val:
                prevOldPtr = nextOldPtr
                nextOldPtr = nextOldPtr.next
            
            if currentNewPtr is None:
                prevNewPtr = currentNewPtr
                newRoot = currentNewPtr = currentOldPtr
            else:
                prevNewPtr = currentNewPtr
                currentNewPtr.next = currentOldPtr
                currentNewPtr =  currentOldPtr
            
            if currentNewPtr.val == prevOldPtr.val and currentNewPtr is not prevOldPtr:
                if prevNewPtr == None:
                    newRoot = currentNewPtr = None
                else:
                    prevNewPtr.next = None
                    currentNewPtr = prevNewPtr

            currentOldPtr = nextOldPtr
        
        if currentNewPtr:
            currentNewPtr.next = None

        return newRoot