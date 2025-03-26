class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def push(self, data):
        newNode = Node(data)
        if self.head == None:
            self.tail = self.head = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode


def startOfLoop(head, meetPoint):
    # len_of_loop = 1
    # ptr1 = ptr2 = meetPoint

    # while ptr1.next != meetPoint:
    #     len_of_loop += 1
    #     ptr1 = ptr1.next

    # ptr1 = ptr2 = head
    # for _ in range(len_of_loop):
    #     ptr1 = ptr1.next

    ptr1 = head
    ptr2 = meetPoint
    while ptr2 != ptr1:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return ptr1


def detectLoop(head):
    if head == None or head.next == None:
        return False

    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if slow != fast:
        return False
    else:
        return startOfLoop(head, slow)


if __name__ == "__main__":
    llist = LList()
    for i in range(1, 6):
        llist.push(i)

    llist.tail.next = llist.head.next

    node = detectLoop(llist.head)
    print(node.data)
