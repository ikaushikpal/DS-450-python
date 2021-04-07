class Node:
    def __init__(self, data):
        self.data = data
        self.next = next


def getNode(data):
    new_node = Node(0)
    new_node.data = data
    new_node.next = new_node.prev = None
    return new_node


def push(head_ref, new_node):

    # since we are adding at the beginning,
    # prev is always None
    new_node.prev = None

    # link the old list off the new node
    new_node.next = (head_ref)

    # change prev of head node to new node
    if ((head_ref) != None):
        (head_ref).prev = new_node

    # move the head to point to the new node
    (head_ref) = new_node
    return head_ref


def revListInGroupOfGivenSize(head, k):
    if k == 0:
        return head

    if head == None or head.next == None:
        return head

    next_node = head
    current_node = prev_node = None
    count = 0
    first_head = last_head = None

    while count < k and next_node:
        if count == 0:
            first_head = next_node

        if next_node.next == None:
            last_head = next_node

        prev_node = current_node
        current_node = next_node
        next_node = next_node.next

        count += 1

        current_node.next = prev_node
        current_node.prev = next_node

    if last_head == None:
        last_head = current_node

    next_head = revListInGroupOfGivenSize(next_node, k)

    if next_head:
        next_head.prev = first_head
    first_head.next = next_head

    return last_head


def printList(node):
    while node is not None:
        if node.next:
            print(node.data, end=" <-> ")
        else:
            print(node.data)
        node = node.next


if __name__ == '__main__':
    head = None

    head = push(head, getNode(8))
    head = push(head, getNode(7))
    head = push(head, getNode(6))
    head = push(head, getNode(5))
    head = push(head, getNode(4))
    head = push(head, getNode(3))
    head = push(head, getNode(2))
    head = push(head, getNode(1))
    k = 3

    print("Original list: ")
    printList(head)

    head = revListInGroupOfGivenSize(head, k)

    print("Modified list: ")
    printList(head)
