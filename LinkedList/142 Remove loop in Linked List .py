def removeLoop(head):
    if head == None:
        return
        
    start = head
    next_next_start = head
    
    while next_next_start != None:
        start = start.next
        next_next_start = next_next_start.next
        
        if next_next_start == None:
            return
            
        next_next_start = next_next_start.next
        
        if start == next_next_start:
            break
    if start == next_next_start:       
        ptr1 = start
        ptr2 = start
         
        # Count the number of nodes in loop
        k = 1
        while(ptr1.next != ptr2):
            ptr1 = ptr1.next
            k += 1
 
        # Fix one pointer to head
        ptr1 = head
         
        # And the other pointer to k nodes after head
        ptr2 = head
        for i in range(k):
            ptr2 = ptr2.next
 
        # Move both pointers at the same place
        # they will meet at loop starting node
        while(ptr2 != ptr1):
            ptr1 = ptr1.next
            ptr2 = ptr2.next
 
        # Get pointer to the last node
        while(ptr2.next != ptr1):
            ptr2 = ptr2.next
 
        # Set the next node of the loop ending node
        # to fix the loop
        ptr2.next = None
        