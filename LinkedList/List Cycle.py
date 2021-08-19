# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, root):
        if root is None:
            return None

        slow = root
        fast = root.next

        while fast and slow != fast:
            slow = slow.next
            fast = fast.next

            if fast:
                fast = fast.next
        
        if fast == None:
            return None
        
        slow = slow.next
        fast = fast.next

        while slow != fast:
            slow=slow.next
            fast = fast.next

        return slow
