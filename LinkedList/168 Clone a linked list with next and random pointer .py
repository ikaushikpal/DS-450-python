class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.arb=None


class Solution:
    def cloneList(self, head):
        clone_head = clone_last = None
        current_node = head

        while current_node:
            if clone_head == None:
                clone_head = clone_last = Node(current_node.data)
            else:
                clone_last.next = Node(current_node.data)
                clone_last = clone_last.next
            current_node = current_node.next

        return clone_head

    def copyPointers(self, original, clone):
        ptr0 = ptr1 = original
        ptr2 = clone

        while ptr1 and ptr2:
            ptr0 = ptr1
            ptr1 = ptr1.next

            ptr0.next = ptr2
            ptr2.arb = ptr0.arb

            ptr2 = ptr2.next
        
        return original, clone

    def makePointers(self, original, clone):
        ptr1 = clone
        while ptr1:
            ptr1.arb = ptr1.arb.arb.next
            ptr1 = ptr1.next
        
        return clone

    def copyList(self, head):
        if not head and not head.next:
            return head

        clone_head = self.cloneList(head)
        head, clone_head = self.copyPointers(head, clone_head)
        return self.makePointers(head, clone_head)



h1 = Node(1)
h2 = Node(2)
h3 = Node(3)

h1.next = h2
h2.next = h3

h1.arb = h3
h3.arb = h2
h2.arb = h1

s = Solution()
x = s.copyList(h1)

class MyDictionary(dict): 
  
    # __init__ function
    def __init__(self):
          
        super().__init__()
        self = dict()
  
        # Function to add key:value
    def add(self, key, value):
          
        # Adding Values to dictionary
        self[key] = value 
        
class Solution:

    def copyList(self, head):
        if not head and not head.next:
            return head
        self.head = head
        return self.clone()
    def clone(self):
          
        # Initialize two references, one 
        # with original list's head.
        original = self.head
        clone = None
  
        # Initialize two references, one 
        # with original list's head.
        mp = MyDictionary()
  
        # Traverse the original list and 
        # make a copy of that
        # in the clone linked list
        while original is not None:
            clone = Node(original.data)
            mp.add(original, clone)
            original = original.next
  
        # Adjusting the original 
        # list reference again.
        original = self.head
  
        # Traversal of original list again
        # to adjust the next and arb 
        # references of clone list using hash map.
        while original is not None:
            clone = mp.get(original)
            clone.next = mp.get(original.next)
            clone.arb = mp.get(original.arb)
            original = original.next
              
        # Return the head reference of the clone list.
        return self.head