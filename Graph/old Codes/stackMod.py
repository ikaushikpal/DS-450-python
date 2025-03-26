class Node():
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.top = None
        self.len = 0
    
    def isEmpty(self):
        if not self.top:
            return True
        return False

    def push(self, value):
        newNode = Node(value)

        if self.isEmpty():
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        
        self.len += 1
    
    def pop(self):
        if not self.isEmpty():
            tempValue = self.top.data
            self.top = self.top.next
            self.len -= 1
            return tempValue
    
    def peek(self):
        if not self.isEmpty():
            return self.top.value

    def __len__(self):
        return self.len
    