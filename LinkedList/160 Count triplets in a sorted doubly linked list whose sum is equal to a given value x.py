from collections import defaultdict


class Node:
    def __init__(self, data):

        self.data = data
        self.next = None
        self.prev = None


def countTriplets(head, key):
    hashTable = defaultdict(lambda: None)
    current_node = head
    count = 0
    # adding all the node values inside hashTable
    while current_node:
        hashTable[current_node.data] = current_node
        current_node = current_node.next

    ptr1 = ptr2 = head
    while ptr1:
        ptr2 = ptr1.next
        while ptr2:
            sum = ptr1.data + ptr2.data

            x = key - sum
            if hashTable[x] != None:
                if hashTable[x] != ptr1 and hashTable[x] != ptr2:
                    count += 1
            ptr2 = ptr2.next
        ptr1 = ptr1.next

    return count//3


def insert(head, data):
    temp = Node(data)
    if ((head) == None):
        (head) = temp
    else:
        temp.next = head
        (head).prev = temp
        (head) = temp
    return head


if __name__ == '__main__':

    head = None

    head = insert(head, 9)
    head = insert(head, 8)
    head = insert(head, 6)
    head = insert(head, 5)
    head = insert(head, 4)
    head = insert(head, 2)
    head = insert(head, 1)

    x = 17

    print("Count = " + str(countTriplets(head, x)))
