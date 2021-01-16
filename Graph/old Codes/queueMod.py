class Node():
    def __init__(self, data = None):
        self.data = data
        self.next = None


class DoublyNode():
    def __init__(self, data = None):
        self.prev = None
        self.data = data
        self.next = None    


class Queue():
    def __init__(self):
        self.front = None
        self.rear = None
        self.len = 0

    def isEmpty(self):
        if self.front == None and self.rear == None:
            return True
        return False

    def enqueue(self, value):
        newNode = Node(value)

        if self.isEmpty():
            self.front = self.rear = newNode
        else:  
            self.rear.next = newNode
            self.rear = newNode
        
        self.len += 1
    
    def peek(self):
        if not self.isEmpty():
            return self.rear.data
    
    def dequeue(self):
        if not self.isEmpty():
            temp = self.front.data
            self.front = self.front.next
            self.len -= 1
            if self.front == None:
                self.rear = None
            return temp
    
    def __contains__(self, value):
        tempFront = self.front
        while tempFront:
            if tempFront.data == value:
                return True
            tempFront = tempFront.next
        
        return False

    def __len__(self):
        return self.len


class Dequeue():
    def __init__(self):
        self.rear = None
        self.front = None
        self.len = 0
    
    def isEmpty(self):
        if not self.rear and not self.front:
            return True
        return False
    
    def enqueueFront(self, value):
        newNode = DoublyNode(value)

        if self.isEmpty():
            self.front = self.rear = newNode
        else:
            newNode.next = self.front
            self.front.prev = newNode
            self.front = newNode
        
        self.len += 1
    
    def enqueueRear(self, value):
        newNode = DoublyNode(value)

        if self.isEmpty():
            self.front = self.rear = newNode
        else:
            newNode.prev = self.rear
            self.rear.next = newNode
            self.rear = newNode
        self.len += 1  
    
    def dequeueFront(self):
        if self.isEmpty():
            return None

        tempValue = self.front.data
        self.front = self.front.next

        if self.front == None:
            self.rear = None   
        else:
            self.front.prev = None

        self.len -= 1
    
    def dequeueRear(self):
        if self.isEmpty():
            return None

        tempValue = self.rear.data
        self.rear = self.rear.prev
        
        if self.rear == None:
            self.rear = None
        else:
            self.rear.next = None
            
        self.len -= 1
    
    def __len__(self):
        return self.len
    
    def __contains__(self, value):
        tempFront = self.front
        while tempFront:
            if tempFront.data == value:
                return True
        return False
    

class circularQueue():
    def __init__(self):
        self.front = None
        self.rear = None
        self.len = 0

    def enqueue(self, value):
        print("happy")
