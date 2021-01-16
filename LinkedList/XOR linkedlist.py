import ctypes 


class Node():
    def __init__(self, data):
        self.data = data
        self.npx = 0
    
    def __str__(self):
        return self.data

        
class XORLinkedList():
    def __init__(self):
        self.headPointer = None
        self.tailPointer = None
        self.__nodes = []
        self.count = 0
    
    def XOR(self, prevNode, nextNode):
        return id(prevNode) ^ id(nextNode)

    def insert_end(self, value):
        newNode = Node(value)

        if(self.tailPointer):
            self.tailPointer.npx = id(newNode) ^ self.tailPointer.npx 
            newNode.npx = id(self.tailPointer)
 
        if self.headPointer is None:
            self.headPointer = newNode

        self.tailPointer = newNode
        self.__nodes.append(newNode)
        self.count += 1

    def insert_before(self, value):
        newNode = Node(value)

        if(self.tailPointer):
            self.headPointer.npx = id(newNode) ^ self.headPointer.npx 
            newNode.npx = id(self.headPointer)
        
        if self.tailPointer is None:
            self.tailPointer = newNode

        self.headPointer = newNode
        self.__nodes.append(newNode)
        self.count += 1

    def delete_first(self):
        if self.headPointer is None:
            return None

        tempData = self.headPointer.data
        self.count -= 1

        if self.headPointer == self.tailPointer: 
            self.headPointer = self.tailPointer = None
            return tempData

        address_of_nextNode = self.headPointer.npx ^ 0
        nextNode = self.__typeCast(address_of_nextNode)

        address_of_nextNextNode = id(self.headPointer) ^ nextNode.npx

        self.headPointer = nextNode
        nextNode.npx = address_of_nextNextNode ^ 0
        return tempData


    def delete_last(self):
        if self.tailPointer is None:
            return None
        
        tempData = self.tailPointer.data
        self.count -= 1

        if self.headPointer == self.tailPointer: 
            self.headPointer = self.tailPointer = None
            return tempData

        address_of_nextNode = self.tailPointer.npx ^ 0
        nextNode = self.__typeCast(address_of_nextNode)

        address_of_nextNextNode = id(self.tailPointer) ^ nextNode.npx

        self.tailPointer = nextNode
        nextNode.npx = address_of_nextNextNode ^ 0
        self.count -= 1

        return tempData

    def __typeCast(self, id): 
        return ctypes.cast(id, ctypes.py_object).value 

    def __len__(self):
        return self.count

    def reverse(self):
        self.headPointer, self.tailPointer = self.tailPointer, self.headPointer

    def display(self, reverse=False):
        if reverse == False:
            print("Printing all Nodes data from head to tail")
            currentNode = self.headPointer
        
        else:
            print("Printing all Nodes data from tail to head")
            currentNode = self.tailPointer


        nextNode, prevNode = 0,0

        while currentNode:
            print(f"{currentNode.data}",end= ' ')
            nextNode = prevNode ^ currentNode.npx
            prevNode = id(currentNode)
            if not nextNode:
                break
            currentNode = self.__typeCast(nextNode)
        print()

if __name__ == "__main__":
    x = XORLinkedList()
    x.insert_end(1)
    x.insert_end(2)
    x.insert_end(3)
    x.insert_end(4)
    x.insert_end(5)
    x.insert_before(6)
    x.display()

    x.delete_first()
    x.display()

    x.delete_last()
    x.display()
    # x.display(reverse=True)
