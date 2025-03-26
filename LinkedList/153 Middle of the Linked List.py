class Solution:
   def middleNode(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow