# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer
    def countAll(self, root):
        ptr = root
        counter = 0
        while ptr:
            counter += 1
            ptr = ptr.next
        
        return counter

    def solve(self, root, n):
        count = self.countAll(root) // 2

        if n > count:
            return -1

        ptr = root

        for i in range(count - n):
            ptr = ptr.next
        
        return ptr.val