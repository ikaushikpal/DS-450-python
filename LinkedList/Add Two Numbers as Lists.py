# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
    def addTwoNumbers(self, root1, root2): #const space
        if not root1 and root2:
            return root2
        
        if root1 and not root2:
            return root1
        
        ptr1, ptr2 = root1, root2
        div = 0
        newRoot = newTail = None

        while ptr1 and ptr2:
            val1 = ptr1.val
            val2 = ptr2.val

            res = val1+val2 + div
            div = res // 10
            val = res % 10
            newNode = ListNode(val)

            if newRoot == None:
                newRoot = newTail = newNode
            else:
                newTail.next = newNode
                newTail= newNode
            
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        while ptr1:
            val1 = ptr1.val

            res = val1 + div
            div = res // 10
            val = res % 10

            newNode = ListNode(val)

            if newRoot == None:
                newRoot = newTail = newNode
            else:
                newTail.next = newNode
                newTail= newNode
            
            ptr1 = ptr1.next

        while ptr2:
            val2 = ptr2.val

            res = val2 + div
            div = res // 10
            val = res % 10
            newNode = ListNode(val)

            if newRoot == None:
                newRoot = newTail = newNode
            else:
                newTail.next = newNode
                newTail= newNode

            ptr2 = ptr2.next
        
        if div:
            if newRoot == None:
                newRoot = newTail = ListNode(1)
            else:
                newTail.next = ListNode(1)
        
        return newRoot

    def addTwoNumbers(self, root1, root2): #O(n) space
        ptr1, ptr2 = root1, root2
        str1 = str2=''

        while ptr1 and ptr2:
            str1 += str(ptr1.val)
            str2 += str(ptr2.val)

            ptr1 = ptr1.next
            ptr2 = ptr2.next

        while ptr1:
            str1 += str(ptr1.val)
            ptr1 = ptr1.next
        
        while ptr2:
            str2 += str(ptr2.val)
            ptr2 = ptr2.next
        
        str1 = str1[::-1]
        str2 = str2[::-1]

        num1, num2 = int(str1), int(str2)
        res = str(num1 + num2)[::-1]

        mainRoot = mainTail = None

        for val in res:
            v = int(val)
            newNode = ListNode(v)

            if mainRoot == None:
                mainRoot = mainTail = newNode
            else:
                mainTail.next = newNode
                mainTail= newNode
        
        return mainRoot






        
