def getNthFromLast(head,n):
    if head == None and head.next == None:
        return head

    count = 0
    current_node = head
    while current_node:
        count += 1
        current_node = current_node.next

    if n > count:
        return -1
    
    current_node = head
    k = count - n
    while k:
        current_node = current_node.next
        k -= 1
    
    return current_node.data