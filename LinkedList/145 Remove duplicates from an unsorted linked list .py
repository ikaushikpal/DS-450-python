def removeDuplicates(head):
    if head == None or head.next == None:
        return head
    tempHead = head
    curr = head

    myDict = {}

    while curr:
        myDict[curr.data] = 1
        nextNode = curr.next
        while (nextNode and nextNode.data == curr.data) or nextNode.data in myDict:
            nextNode = nextNode.next
        
        curr.next = nextNode
        curr = nextNode
    
    return tempHead

    
