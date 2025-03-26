# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list

    # Time Complexity : O(n)
    # Space Complexity : O(n)
    def reorderList(self, root):
        if not root or not root.next:
            return root
        
        linkedListAddresses = []
        ptr = root
        while ptr:
            linkedListAddresses.append(ptr)
            ptr = ptr.next
        
        i, j = 0, len(linkedListAddresses)-1
        main_head = main_tail= None

        while i<=j:
            leftNode, rightNode = linkedListAddresses[i], linkedListAddresses[j]

            if main_head == None:
                main_head = leftNode
                main_head.next = rightNode
                main_tail = rightNode

            else:
                main_tail.next = leftNode
                main_tail = leftNode
                main_tail.next = rightNode
                main_tail = rightNode
            
            i += 1
            j -= 1
        
        if main_tail:
            main_tail.next = None
        
        return main_head

# Efficient Solution:

# 1) Find the middle point using tortoise and hare method.
# 2) Split the linked list into two halves using found middle point in step 1.
# 3) Reverse the second half.
# 4) Do alternate merge of first and second halves.

# Time Complexity : O(n)
# Space Complexity : O(1)

    def reverseLL(self, root):
        prevNode = currentNode = None
        nextNode = root

        while nextNode:
            prevNode = currentNode
            currentNode = nextNode
            nextNode = nextNode.next

            currentNode.next = prevNode

        return currentNode

    def splitLL(self, root):
        if root is None:
            return None, None

        slow = root
        fast = root.next
        prev = None

        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

            if fast:
                fast = fast.next
        
        head1 = root
        prev.next = None
        head2 = slow

        return head1, head2

    def reorderList(self, root):
        if not root or not root.next:
            return root
        
        leftHead, rightHead = self.splitLL(root)
        rightHead = self.reverseLL(rightHead)

        leftPtr, rightPtr = leftHead, rightHead
        main_head = main_tail = None

        while leftPtr and rightPtr:
            if main_head == None:
                main_head = main_tail = leftPtr
            else:
                main_tail.next = leftPtr
                main_tail = leftPtr
            
            leftPtr = leftPtr.next

            main_tail.next = rightPtr
            main_tail = rightPtr

            rightPtr = rightPtr.next
        
        if rightPtr: #if odd no of nodes then
            main_tail.next = rightPtr
            main_tail = rightPtr

        if main_tail:
            main_tail.next = None
        
        return main_head

# both approach took same time , lol
root = ListNode(10)
root.next = ListNode(20)
root.next.next = ListNode(30)
root.next.next.next = ListNode(40)

x = Solution().reorderList(root)

while x:
    print(x.val, end=' ')
    x = x.next