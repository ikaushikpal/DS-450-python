def findIntersection(head1,head2):
    if head1 == None:
        return head2
    if head2 == None:
        return head1  

    head3 = None
    ptr1 = head1
    ptr2 = head2
    ptr3 = head3

    while ptr1 and ptr2:
        if ptr1.data == ptr2.data:
            newNode = Node(ptr1.data)
            if head3 == None:
                head3 = ptr3 = newNode
            else:
                ptr3.next = newNode
                ptr3 = newNode
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        elif ptr1.data > ptr2.data:
            ptr2 = ptr2.next
        else:
            ptr1 = ptr1.next
 
    return head3