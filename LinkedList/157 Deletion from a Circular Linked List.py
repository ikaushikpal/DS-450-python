class Node:
	def __init__(self, next = None, data = None):
		self.next = next
		self.data = data

# Function to insert a node at the beginning of
# a Circular linked list
def push(head_ref, data):

	# Create a new node and make head as next
	# of it.
	ptr1 = Node()
	ptr1.data = data
	ptr1.next = head_ref

	# If linked list is not None then set the
	# next of last node
	if (head_ref != None) :
		
		# Find the node before head and update
		# next of it.
		temp = head_ref
		while (temp.next != head_ref):
			temp = temp.next
		temp.next = ptr1
	
	else:
		ptr1.next = ptr1 # For the first node

	head_ref = ptr1
	return head_ref

# Function to print nodes in a given
# circular linked list
def printList( head):

	temp = head
	if (head != None) :
		while(True) :
			print( temp.data, end = " ")
			temp = temp.next
			if (temp == head):
				break
	print()

# Function to delete a given node from the list
def deleteNode(head, key) :
	if head is None:
		return None

	prev_node, next_node = None, None
	current_node = head
	tempHead = head

	while next_node != tempHead:
		next_node = current_node.next
		if current_node.data == key:
			break
		prev_node = current_node
		current_node = next_node

	# if key node is in between 2nd node to last node
	if prev_node:
		prev_node.next = next_node
		return head

	# if ll has only 1 node and that node need to delete
	if next_node == current_node:
		return None

	# if key node is first node of circular ll
	if current_node == head:
		while current_node.next != head:
			current_node = current_node.next
		
		current_node.next = next_node
		return next_node

head = None
head = push(head, 2)
head = push(head, 5)
head = push(head, 7)
head = push(head, 8)
head = push(head, 10)

print("List Before Deletion: ")
printList(head)

head = deleteNode(head, 10)

print( "List After Deletion: ")
printList(head)

