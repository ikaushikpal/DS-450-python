def removeDuplicates(head):
    if head == None or head.next == None:
        return
    curr = head
    while curr:
        nextNode = curr.next
        while nextNode and nextNode.data == curr.data:
            nextNode = nextNode.next
        
        curr.next = nextNode
        curr = nextNode
    
