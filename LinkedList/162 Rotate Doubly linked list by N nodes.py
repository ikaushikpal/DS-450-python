class Node:
    def __init__(self, next=None,
                 prev=None, data=None):
        self.next = next  # reference to next node in DLL
        self.prev = prev  # reference to previous node in DLL
        self.data = data


def push(head, new_data):

    new_node = Node(data=new_data)

    new_node.next = head
    new_node.prev = None

    if head is not None:
        head.prev = new_node

    head = new_node
    return head


def printList(node):
    while node is not None:
        if node.next:
            print(node.data, end=" <-> ")
        else:
            print(node.data)
        node = node.next


def rotate(start, N):
    if N == 0:
        return start

    count_nodes = 0
    current_node = head
    last_node = None
    first_node = head

    while current_node:
        if current_node.next == None:
            last_node = current_node

        count_nodes += 1
        current_node = current_node.next

    pos = N % count_nodes
    last_node.next = first_node
    first_node.prev = last_node

    current_node = first_node
    while N:
        current_node = current_node.next
        N -= 1

    prev_node = current_node.prev
    current_node.prev = prev_node.next = None

    return current_node


if __name__ == "__main__":
    head = None

    head = push(head, 'e')
    head = push(head, 'd')
    head = push(head, 'c')
    head = push(head, 'b')
    head = push(head, 'a')

    print("Before Rotation")
    printList(head)

    N = 2
    head = rotate(head, N)

    print("After Rotation")
    printList(head)
