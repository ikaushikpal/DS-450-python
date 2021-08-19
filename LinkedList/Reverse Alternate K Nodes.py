# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseK(self, root, k, rev):
        if not root or not root.next:
            return root

        currentNode = prevNode = None
        nextNode = root
        count = 0

        while nextNode and count < k:
            prevNode = currentNode
            currentNode = nextNode
            nextNode = nextNode.next

            if rev == True:
                currentNode.next = prevNode

            count += 1

            if rev == True:
                root.next = self.reverseK(nextNode, k, False)
                return currentNode

            else:
                currentNode.next = self.reverseK(nextNode, k, True)
                return root
                
    def solve(self, root, k):
        return self.reverseK(root, k, True)


# 42 -> 68 -> 35 -> 1
root = ListNode(42)
root.next = ListNode(68)
root.next.next = ListNode(35)
root.next.next.next = ListNode(1)

x = Solution().solve(root, 2)
ptr = x

while ptr:
    print(ptr.val, end=' ')
    ptr = ptr.next
