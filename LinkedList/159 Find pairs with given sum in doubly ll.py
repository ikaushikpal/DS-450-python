# Python3 program to find a pair with
class Node:
	def __init__(self, x):

		self.data = x
		self.next = None
		self.prev = None


def pairSum(head, x):
	head1 = head
	head2 = head

	while (head2.next != None):
		head2 = head2.next

	flag = False

	while (head1 != None and head2 != None and
		head1 != head2 and head2.next != head1):

		# Pair flag
		if head1.data + head2.data == x:
			flag = True
			print("(", head1.data, ",", head2.data, ")", end=' ')

			head1 = head1.next
			head2 = head2.prev

		elif head1.data + head2.data < x:
			head1 = head1.next

		else:
			head2 = head2.prev

	if flag == False:
		print("No pairs Found")
	else:
	  print()

def insert(head, data):
	
	temp = Node(data)
	
	if not head:
		head = temp
	else:
		temp.next = head
		head.prev = temp
		head = temp
		
	return head

# Driver code
if __name__ == '__main__':
	
	head = None
	head = insert(head, 9)
	head = insert(head, 8)
	head = insert(head, 6)
	head = insert(head, 5)
	head = insert(head, 4)
	head = insert(head, 2)
	head = insert(head, 1)
	x = 7

	pairSum(head, x)
