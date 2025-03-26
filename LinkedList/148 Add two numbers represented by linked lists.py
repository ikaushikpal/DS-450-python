def reverse(head):
    current = None
    prevNode = None
    nextNode = head

    while nextNode:
        prevNode = current
        current = nextNode
        nextNode = nextNode.next

        current.next = prevNode
    
    return current

def addTwoLists(first, second):
    if first == None:
        return second

    if second == None:
        return first

    reversedFirst = reverse(first)
    reversedSecond = reverse(second)
    third = None

    ptr1 = reversedFirst
    ptr2 = reversedSecond
    ptr3 = third

    result = remainder = 0

    while ptr1 and ptr2:
        result = ptr1.data + ptr2.data + remainder
        remainder = result // 10
        newNode = Node(result % 10)

        if ptr3 == None:
            third = ptr3 = newNode
        else:

            ptr3.next = newNode
            ptr3 = newNode
        
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    
    while ptr1:
        result = ptr1.data + remainder
        remainder = result // 10
        newNode = Node(result % 10)

        if ptr3 == None:
            third = ptr3 = newNode
        else:

            ptr3.next = newNode
            ptr3 = newNode
        
        ptr1 = ptr1.next
    
    while ptr2:
        result = ptr2.data + remainder
        remainder = result // 10
        newNode = Node(result % 10)

        if ptr3 == None:
            third = ptr3 = newNode
        else:

            ptr3.next = newNode
            ptr3 = newNode
        
        ptr2 = ptr2.next

    if remainder != 0:
        ptr3.next = Node(remainder)

    return reverse(third)        





