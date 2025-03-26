# Given an integer N, find its factorial.

# Example 1:
# Input: N = 5
# Output: 120
# Explanation : 5! = 1*2*3*4*5 = 120


# Example 2:
# Input: N = 10
# Output: 3628800
# Explanation :
# 10! = 1*2*3*4*5*6*7*8*9*10 = 3628800

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class LLMath:
    def reprNum(self, num):
        head = tail = None

        while num:
            rem = num % 10
            if head is None:
                head = tail = Node(rem)
            else:
                tail.next = Node(rem)
                tail = tail.next
            num = num // 10 
        
        return head

    def reprStr(self, root):
        s = ''
        while root:
            s += str(root.data)
            root = root.next
        return reversed(s)

    def mul(self, root1, root2):
        resHead = resTail = ptr3 = None
        ptr1, ptr2 = root1, root2
        extra = 0

        while ptr2:
            while ptr1:
                v = ptr1.data * ptr2.data + extra
                d = v % 10
                if ptr3:
                    ptr3
                ptr1 = ptr1.next
            ptr2 = ptr2.next


class Solution:
    def factorial(self, N):
        pass