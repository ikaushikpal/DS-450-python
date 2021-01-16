def detectLoop(head):
    if head == None:
        return False
        
    start = head
    next_next_start = head.next
    
    if next_next_start == None:
        return False
    
    next_next_start = head.next.next
    while next_next_start != None:
        start = start.next
        next_next_start = next_next_start.next
        
        if next_next_start == None:
            return False
            
        next_next_start = next_next_start.next
        
        if start == next_next_start:
            return True
        
    return False

