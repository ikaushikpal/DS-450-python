class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next



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

def addOne(head):
    if head == None:
        return head

    tempHead = reverse(head)
    currentNode = tempHead
    remainder = 1
    prevNode = None
    
    while currentNode:
        if currentNode.data < 9:
            currentNode.data += 1
            remainder = 0
            break
        else:
            currentNode.data = 0
            remainder = 1
            
        prevNode = currentNode
        currentNode = currentNode.next
    
    if remainder != 0:
        prevNode.next = Node(remainder)
        
    return reverse(tempHead)



head = Node(9)
head.next = Node(9)
head.next.next = Node(9)

head = addOne(head)

while head:
    print(head.data,end='')
    head = head.next