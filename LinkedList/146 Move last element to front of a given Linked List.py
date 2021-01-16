def lastElementToFront(head):
    if head == None or head.next == None:
        return head
    
    current = prev = head

    while current.next:
        prev = current
        current = current.next

    current.next = head
    prev.next = None
    head = current
    return current