def getLength(head):
    curr = head
    count = 1
    while curr:
        curr = curr.next
        count += 1   
    return count

def intersetPoint(head1,head2):
    if head1 == None or head2 == None:
        return -1

    ptr1 = head1
    ptr2 = head2

    len_of_head1 = getLength(head1)
    len_of_head2 = getLength(head2)

    if len_of_head1 > len_of_head2 :
        diff = len_of_head1 - len_of_head2
        for _ in range(diff):
            ptr1 = ptr1.next
    
    if len_of_head1 < len_of_head2 :
        diff = len_of_head2 - len_of_head1
        for _ in range(diff):
            ptr2 = ptr2.next

    while ptr1 and ptr2:
        if ptr1.data == ptr2.data:
            return ptr1.data

        ptr2 = ptr2.next
        ptr1 = ptr1.next

    return -1
def intersetPointV2(head1,head2):
    ptr1 = head1
    ptr2 = head2

    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

        if ptr1.data == ptr2.data:
            return ptr1.data
        
        if ptr1 == None:
            ptr1 = head2
        
        if ptr2 == None:
            ptr2 = head1

    return -1