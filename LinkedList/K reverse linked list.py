class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
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