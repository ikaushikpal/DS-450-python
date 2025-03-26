class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        if not self.head:
            return None

        next_node = self.head
        prev_node = current_node = None
        head2 = None

        while next_node:
            if next_node.next == None:
                head2 = next_node
                
            prev_node = current_node
            current_node = next_node
            next_node = next_node.next

            current_node.next = prev_node
            current_node.prev = next_node

        self.head = head2

    def push(self, new_data):

        # 1. Allocates node
        # 2. Put the data in it
        new_node = Node(new_data)

        # 3. Make next of new node as head and
        # previous as None (already None)
        new_node.next = self.head

        # 4. change prev of head node to new_node
        if self.head is not None:
            self.head.prev = new_node

        # 5. move the head to point to the new node
        self.head = new_node

    def printList(self, node):
        while(node is not None):
            print(node.data,end=' ')
            node = node.next
        print()



dll = DoublyLinkedList()
dll.push(2)
dll.push(4)
dll.push(8)
dll.push(10)

print("Original Linked List")
dll.printList(dll.head)

# Reverse doubly linked list
dll.reverse()

print("Reversed Linked List")
dll.printList(dll.head)

