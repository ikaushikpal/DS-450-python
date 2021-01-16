def splitList(head):
    if head == None:
        return None,None
    
    count = 1
    slow = fast = head

    while fast.next != head or fast.next.next != head:
        slow = slow.next
        fast = fast.next.next
    
    if fast.next == head:
        fast.next = None
    
    elif fast.next.next == head:
        fast.next.next = None

    head2 = slow.next  
    slow.next   = None
    
    return head, head2 

    
