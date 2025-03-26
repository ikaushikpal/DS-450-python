# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
    def partition(self, root, x):
        left_head = left_tail = None
        right_head = right_tail = None
        ptr = root

        while ptr:
            if ptr.val < x:
                if left_head is None:
                    left_head = left_tail = ptr
                else:
                    left_tail.next = ptr
                    left_tail = ptr

            else:
                if right_head is None:
                    right_head = right_tail = ptr
                else:
                    right_tail.next = ptr
                    right_tail = ptr
            ptr = ptr.next
        

        if left_head:
            main_head = left_head
            left_tail.next = right_head
        else:
            main_head = right_head

        if right_tail:
            right_tail.next = None
        
        return main_head
