from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def storeLinkedList(self, head, storedAddress):
        if head is None:
            return

        storedAddress.append(head)
        self.storeLinkedList(head.next, storedAddress)
        return storedAddress

    def builtTree(self, storedAddress, low, high):
        if low > high: return None

        mid = (low + high) // 2
        head = storedAddress[mid]
        root = TreeNode(head.val)

        root.left = self.builtTree(storedAddress, low, mid-1)
        root.right = self.builtTree(storedAddress, mid+1, high)

        return root
        
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # if empty linkedlist given
        if head == None: return None
        
        storedAddress = self.storeLinkedList(head, [])
        
        return self.builtTree(storedAddress, 0, len(storedAddress)-1)