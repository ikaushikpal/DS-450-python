class Solution():
    def reverse(self, head):
        next_node = head
        prev_node = current_node = None

        while next_node:
            prev_node = current_node
            current_node =next_node
            next_node = next_node.next

            current_node.next = prev_node
        head.next = None
        return current_node

    def compute_util(self, head):
        next_node = head
        current_node = None
        max_node = head

        while next_node and next_node.next:
            current_node = next_node
            next_node = next_node.next

            if next_node.data < max_node.data:
                current_node.next = next_node.next
                next_node = current_node
            else:
                max_node = next_node

        return head

    def compute(self, head):
        if head == None or head.next == None:
            return head
            
        head = self.reverse(head)
        head = self.compute_util(head)
        return self.reverse(head)
