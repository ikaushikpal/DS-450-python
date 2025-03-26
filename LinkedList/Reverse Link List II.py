# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or not head.next:
            return head
        
        dummy = ptr = ListNode(None, head)
        for _ in range(left - 1):
            ptr = ptr.next
        
        leftTail = ptr
        revTail = ptr.next
        
        # revserse
        prevNode = currNode = None
        nextNode = ptr.next
        for _ in range(right - left + 1):
            prevNode = currNode
            currNode = nextNode
            nextNode = nextNode.next
            currNode.next = prevNode
        
        revHead = currNode
        rightHead = nextNode
        
        # linking
        leftTail.next = revHead
        revTail.next = rightHead
        
        return dummy.next
# Time Complexity: O(N)
# Space Complexity: O(1)


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)

m = 2
n = 3

x = Solution().reverseBetween(root, m, n)

ptr = x
while ptr:
	print(ptr.val, end=' ')
	ptr = ptr.next
