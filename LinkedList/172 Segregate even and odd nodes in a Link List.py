class Solution:
    def divide(self, N, head):
        if head == None or head.next == None:
            return head

        odd_head = even_head = None
        odd_last = even_last = None
        current_node = head

        while current_node:
            if current_node.data % 2 != 0:
                if odd_head == None:
                    odd_head = odd_last = current_node
                else:
                    odd_last.next = current_node
                    odd_last = current_node
                
            else:
                if even_head == None:
                    even_head = even_last = current_node
                else:
                    even_last.next = current_node
                    even_last = current_node
                
            current_node = current_node.next

        if even_head == None:
            if odd_last:
                odd_last.next = None
            return odd_head
        else:
            even_last.next = odd_head
            if odd_last:
                odd_last.next = None
            return even_head
