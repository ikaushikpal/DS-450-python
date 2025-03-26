class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    #shortCut MEthod
    def solve(self, root):
        if not root or not root.next:
            return root
        
        xNode = yNode = None
        ptr = root.next
        counter = 0
        vals = []

        while ptr:
            if counter%2 == 0:
                vals.append(ptr.val)
            counter += 1
            ptr = ptr.next
        
        ptr = root.next
        counter = 0
        while ptr:
            if counter%2 == 0:
                ptr.val = vals.pop()

            counter += 1
            ptr = ptr.next

        return root

    def reverseLL(self, root):
        prevNode = currentNode = None
        nextNode = root

        while nextNode:
            prevNode = currentNode
            currentNode = nextNode
            nextNode = nextNode.next

            currentNode.next = prevNode
        
        return currentNode

    def solveAnother(self, root):
        if not root or not root.next:
            return root
        
        evenNodeHead = evenNodeTail = None
        oddNodeHead = oddNodeTail = None
        count = 1
        ptr = root

        while ptr:
            if count%2 == 0:
                # evenNode
                if evenNodeHead == None:
                    evenNodeHead = evenNodeTail = ptr
                else:
                    evenNodeTail.next = ptr
                    evenNodeTail = ptr
            else:
                if oddNodeHead == None:
                    oddNodeHead = oddNodeTail = ptr
                else:
                    oddNodeTail.next = ptr
                    oddNodeTail = ptr
            
            count += 1
            ptr = ptr.next
        
        evenNodeTail.next = oddNodeTail.next = None
        #reverse even node LL
        evenNodeHead = self.reverseLL(evenNodeHead)

        evenPtr, evenPtrNext = evenNodeHead, evenNodeHead.next
        oddPtr, oddPtrNext = oddNodeHead, oddNodeHead.next
        mainHead = mainTail = None

        while evenPtr and oddPtr:
            if mainHead == None:
                mainHead = mainTail = oddPtr
                mainTail.next = evenPtr
                mainTail = evenPtr
            
            else:
                mainTail.next = oddPtr
                mainTail = oddPtr
                mainTail.next = evenPtr
                mainTail = evenPtr
            
            evenPtr = evenPtrNext
            oddPtr = oddPtrNext
            if evenPtrNext:
                evenPtrNext = evenPtrNext.next
            if oddPtrNext:
                oddPtrNext = oddPtrNext.next
        
        if oddPtr:
            mainTail.next = oddPtr
        
        return mainHead



root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
root.next.next.next.next = Node(5)
root.next.next.next.next.next = Node(6)

x = Solution().solveAnother(root)
ptr = x
while ptr:
    print(ptr.val, end=' ')
    ptr=ptr.next