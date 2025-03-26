class LinkedList(object):
    def __init__(self):
         self.head = None
  

    class Node(object):
        def __init__(self, d):
            self.data = d
            self.next = None
  

    def segregate(self, head):
        main_head = zero_head = one_head = two_head = None
        zero_last = one_last = two_last = None

        current_node = head
        while current_node:
            if current_node.data == 0:
                if zero_head is None:
                    zero_head = zero_last = current_node
                else:
                    zero_last.next = current_node
                zero_last = current_node

            elif current_node.data == 1:
                if one_head is None:
                    one_head = one_last = current_node
                else:
                    one_last.next = current_node
                one_last = current_node
            else:
                if two_head is None:
                    two_head = two_last = current_node
                else:
                    two_last.next = current_node
                two_last = current_node

            current_node = current_node.next
        
        if zero_head != None:
            main_head = zero_head
            if one_head != None:

                zero_last.next = one_head
                if two_head != None:
                    one_last.next = two_head
                    two_last.next = None
                else:
                    one_last.next = None
            else:

                if two_head != None:
                    zero_last.next = two_head
                    two_last.next = None
                else:
                    zero_last.next = None
        
        elif one_head != None:
            main_head = one_head

            if two_head != None:
                one_last.next = two_head
                two_last.next = None
            else:
                one_last.next = None

        elif two_head != None:
            main_head = two_head
            two_last.next = None
        else:
            main_head = None
        
        return main_head


    def push(self, new_data):
        new_node = self.Node(new_data)
  
        # 3. Make next of new Node as head
        new_node.next = self.head
  
        # 4. Move the head to point to new Node
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp != None:
            print(str(temp.data),end=' ')
            temp = temp.next
        print()



if __name__ == "__main__":
    llist = LinkedList()
    llist.push(0)
    llist.push(1)
    llist.push(0)
    llist.push(2)
    llist.push(1)
    llist.push(1)
    llist.push(2)
    llist.push(1)
    llist.push(2)
    
    print("Linked List before sorting")
    llist.printList()
    
    llist.head = llist.segregate(llist.head)
    
    print("Linked List after sorting")
    llist.printList()
