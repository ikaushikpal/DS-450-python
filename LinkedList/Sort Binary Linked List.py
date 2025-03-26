# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, root):
        one_head = one_tail = None
        zero_head = zero_tail = None
        ptr = root

        while ptr:
            if ptr.val == 1:
                if one_head is None:
                    one_head = one_tail = ptr
                else:
                    one_tail.next = ptr
                    one_tail = ptr

            else:
                if zero_head is None:
                    zero_head = zero_tail = ptr
                else:
                    zero_tail.next = ptr
                    zero_tail = ptr
            ptr = ptr.next
        
        main_head = zero_head
        if zero_tail:
            zero_tail.next = one_head
        
        if one_tail:
            one_tail.next = None
        
        return main_head
