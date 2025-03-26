# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.

# Given the head of a linked list with even length, return the maximum twin sum of the linked list.

 

# Example 1:
# Input: head = [5,4,2,1]
# Output: 6
# Explanation:
# Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
# There are no other nodes with twins in the linked list.
# Thus, the maximum twin sum of the linked list is 6. 


# Example 2:
# Input: head = [4,2,2,3]
# Output: 7
# Explanation:
# The nodes with twins present in this linked list are:
# - Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
# - Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
# Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 


# Example 3:
# Input: head = [1,100000]
# Output: 100001
# Explanation:
# There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.



from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def split(self, head):
        slow = fast = head
        
        while fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        nextHead = slow.next
        slow.next = None
        
        return head, nextHead
    
    def reverse(self, head):
        slow = prev = None
        fast = head
        
        while fast:
            prev = slow
            slow = fast
            fast = fast.next
            
            slow.next = prev
        return slow
    
    def findMaximum(self, head1, head2):
        ptr1, ptr2 = head1, head2
        maximumSum = 0
        
        while ptr1 and ptr2:
            val1 = int(ptr1.val)
            val2 = int(ptr2.val)
            
            maximumSum = max(maximumSum, val1 + val2)
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return maximumSum
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        head1, head2 = self.split(head)
        head2 = self.reverse(head2)
        return self.findMaximum(head1, head2)
# Time Complexity: O(N/2 + N/2 + N/2) = O(N)
# Space Complexity: O(1)


if __name__ == "__main__":
    sol = Solution()