def revserseI(head):
    next_node = head
    prev_node = current_node = None

    while next_node:
        prev_node = current_node
        current_node =next_node
        next_node = next_node.next

        current_node.next = prev_node
    head.next = None
    return current_node

def reverseR(head):
    if head or head.next == None:
        return head
    
    x = reverseR(head.next)
    
    # head's next is x so x's next = head
    head.next.next = head
    head.next = None # making x's next's next = None

    return x
