class Node():
    def __init__(self, data = None):
        self.data = data
        self.next = None



class Solution:
    def mergeSortedLinkedList(self, head1, head2):
        if head1 == None:
            return head2
        
        if head2 == None:
            return head1
            
        main_head = last_node = None
        ptr1 = head1
        ptr2 = head2

        while ptr1 and ptr2:
            if ptr1.data < ptr2.data:
                if not main_head:
                    main_head = last_node = ptr1
                else:
                    last_node.next = ptr1
                    last_node = ptr1
                ptr1 = ptr1.next
            else:
                if not main_head:
                    main_head = last_node = ptr2
                else:
                    last_node.next = ptr2
                    last_node = ptr2
                ptr2 = ptr2.next
        
        while ptr1:
            last_node.next = ptr1
            last_node = ptr1
            ptr1 = ptr1.next

        while ptr2:
            last_node.next = ptr2
            last_node = ptr2
            ptr2 = ptr2.next

        if last_node:
            last_node.next = None
        
        return main_head

    def splitLinkedList(self, head):
        if head == None or head.next == None:
            return head
        
        slow = head
        fast = head.next
        head1 = head2 = None

        while fast:
            fast = fast.next
            if fast:
                slow = slow.next
                fast = fast.next

        head1 = head
        head2 = slow.next
        slow.next = None

        return head1, head2

    def mergeSort(self, head):
        if head == None or head.next == None:
            return head

        h1, h2 = self.splitLinkedList(head)
        left = self.mergeSort(h1)
        right = self.mergeSort(h2)

        new_head = self.mergeSortedLinkedList(left, right)
        return new_head



h = Node(10)
h.next = Node(5)
h.next.next = Node(15)


s = Solution()
x = s.mergeSort(h)