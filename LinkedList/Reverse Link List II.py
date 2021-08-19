# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @param C : integer
	# @return the head node in the linked list
	def reverseBetween(self, root, m, n):
		if not root or not root.next:
			return root

		count = 0
		prev = None
		ptr = root
		newHead = None

		while count < m-1:
			prev = ptr
			ptr = ptr.next
			count += 1

		prevNode = currentNode = None
		nextNode = ptr

		while nextNode and count < n:
			prevNode = currentNode
			currentNode = nextNode
			nextNode = nextNode.next

			currentNode.next = prevNode

			count += 1

		if prev == None:
			newHead = currentNode
			root.next = nextNode
			return newHead

		else:
			tail = prev.next
			prev.next = currentNode
			tail.next = nextNode
			return root


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
