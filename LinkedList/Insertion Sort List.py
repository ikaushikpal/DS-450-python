# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def insertionSortList(self, root):
 
        # Initialize sorted linked list
        sorted_root = None
    
        # Traverse the given linked list and insert every
        # node to sorted
        currentNode = root
        while (currentNode != None):
        
            # Store next for next iteration
            nextNode = currentNode.next
    
            # insert currentNode in sorted linked list
            sorted_root = self.sortedInsert(sorted_root, currentNode)
    
            # Update currentNode
            currentNode = nextNode
        
        # Update root to point to sorted linked list
        root = sorted_root
        return root
    
    # function to insert a new_node in a list. Note that this
    # function expects a pointer to head_ref as this can modify the
    # head of the input linked list (similar to push())
    def sortedInsert(self, head_ref, new_node):
    
        currentNode = None
        
        # Special case for the head end */
        if (head_ref == None or (head_ref).data >= new_node.data):
        
            new_node.next = head_ref
            head_ref = new_node
        
        else:
        
            # Locate the node before the point of insertion
            current = head_ref
            while (current.next != None and
                current.next.data < new_node.data):
            
                current = current.next
            
            new_node.next = current.next
            current.next = new_node
            
        return head_ref


