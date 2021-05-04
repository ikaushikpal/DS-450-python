class DLLNode:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
 
 
''' Representation of the stack
data structure that supports
findMiddle() in O(1) time. The
Stack is implemented using
Doubly Linked List. It maintains
pointer to head node, pointer
to middle node and count of
nodes '''
 
 
class myStack:
    def __init__(self):
        self.__head = None
        self.__mid = None
        self.__count = 0
        self.__midIndex = -1
    
    def push(self, data)->None:
        self.__count += 1
        newNode = DLLNode(data)

        if self.__head == None:
            self.__head = self.__mid = newNode
            self.__midIndex = 0  

        else:
            self.__head.next = newNode
            newNode.prev = self.__head
            self.__head = newNode

            if self.__count //2 > self.__midIndex :
                self.__midIndex += 1
                self.__mid = self.__mid.next
    
    def pop(self):
        if self.__count == 0:
            return None
        
        self.__count -= 1
        data = self.__head.data

        if self.__count // 2 < self.__midIndex:
            self.__mid = self.__mid.prev
            self.__midIndex -= 1
        
        prevNode = self.__head.prev
        if prevNode == None:
            self.__mid = self.__head = None
            self.__midIndex = -1
        else:
            prevNode.next = None
            self.__head.prev = None
            self.__head = prevNode
        
        return data
    
    def top(self):
        if self.__count == 0:
            return None
        return self.__head.data
    
    def findMiddle(self):
        if self.__count == 0:
            return None
        return self.__mid.data
    
    def deleteMiddle(self):
        if self.__count == 0:
            return None
        
        self.__count -= 1
        self.__midIndex -= 1
        data = self.__mid.data

        prevNode = self.__mid.prev
        nextNode = self.__mid.next  

        if prevNode == None:
            self.__mid = self.__head = None
            self.__midIndex = -1
        else:
            self.__mid.prev = self.__mid.next = None
            prevNode.next = nextNode
            nextNode.prev = prevNode
            self.__mid = prevNode

        return data


if __name__ == '__main__':
    stack = myStack()
    stack.push(10)
    print(stack.findMiddle())
    stack.push(20)
    stack.push(30)

    print(stack.findMiddle())
    print(stack.deleteMiddle())
    stack.push(40)

    print(stack.findMiddle())
    print(stack.pop())
    print(stack.top())


    print(stack.findMiddle())
    print(stack.pop())
    print(stack.top())


    print(stack.findMiddle())
    print(stack.pop())
    print(stack.pop())