# def isPalindrome(head):
#     currentNode = head
#     myList = []
#     while currentNode:
#         myList.append(currentNode.data)
#         currentNode = currentNode.next
    
#     i = 0
#     j = len(myList) - 1
#     while i<=j:
#         if myList[i] != myList[j]:
#             return False
#         i += 1
#         j -= 1
#     return True


def reverse(head):
    currentNode = prevNode = None
    nextNode = head
    while nextNode:
        prevNode = currentNode
        currentNode = nextNode
        nextNode = nextNode.next

        currentNode.next = prevNode
    
    return currentNode

def isPalindrome(head):
    if head == None or head.next == None:
        return True
        
    slow = fast = head
    prev = None
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    head2 = slow
    prev.next = None
    
    ptr1 = head
    ptr2 = reverse(head2)
    
    while ptr1 and ptr2:
        if ptr1.data != ptr2.data:
            return False
        
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return True