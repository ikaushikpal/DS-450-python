# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
# @param A : head node of linked list
# @return an integer
    def splitLL(self, root):
        head1, head2 = None, None
        head1 = slow = root
        fast = root.next

        while fast:
            fast = fast.next
            if fast:
                slow = slow.next
                fast = fast.next
        
        head2 = slow.next
        slow.next = None

        return (head1, head2)

    def reverseLL(self, root):
        prev = curr = None
        next = root

        while next:
            prev = curr
            curr = next
            next = next.next

            curr.next = prev

        return curr

    def lPalin(self, root):
        if root is None:
            return True
        
        head1, head2 = self.splitLL(root)
        head2 = self.reverseLL(head2)

        ptr1, ptr2 = head1, head2

        while ptr1 and ptr2:
            if ptr1.val != ptr2.val:
                return 0

            ptr1 = ptr1.next
            ptr2 = ptr2.next
        

        return 1
