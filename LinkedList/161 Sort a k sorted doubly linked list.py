import heapq


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def sortKSortedDLL(head, k):
    heap = []
    current_node = head
    for _ in range(k + 1):
        heapq.heappush(heap, current_node.data)
        current_node = current_node.next

    ptr1 = head

    while len(heap):
        x = heapq.heappop(heap)
        ptr1.data = x
        ptr1 = ptr1.next

        if current_node:
            heapq.heappush(heap, current_node.data)
            current_node = current_node.next

    return head


def insert(head, data):
    temp = Node(data)
    if (head) == None:
        (head) = temp
    else:
        temp.next = head
        (head).prev = temp
        (head) = temp
    return head


def printList(node):
    while node is not None:
        if node.next:
            print(node.data, end=" <-> ")
        else:
            print(node.data)
        node = node.next


if __name__ == "__main__":

    head = None
    head = insert(head, 8)
    head = insert(head, 56)
    head = insert(head, 12)
    head = insert(head, 2)
    head = insert(head, 6)
    head = insert(head, 3)

    print("Before Sorting")
    printList(head)

    k = 2
    head = sortKSortedDLL(head, k)

    print("After Sorting")
    printList(head)
