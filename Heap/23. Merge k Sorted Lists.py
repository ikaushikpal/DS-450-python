# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.


# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Example 2:
# Input: lists = []
# Output: []

# Example 3:
# Input: lists = [[]]
# Output: []
 

# Constraints:
# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.

import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        # only to fix TypeError
        clock = 0

        for head in lists:
            if head:
                min_heap.append((head.val, clock, head))
            clock += 1

        heapq.heapify(min_heap)
        main_ptr = main_head = ListNode(None)

        while min_heap:
            *_, ptr = heapq.heappop(min_heap)

            main_ptr.next = ptr
            main_ptr = main_ptr.next

            if ptr.next:
                ptr = ptr.next
                heapq.heappush(min_heap, (ptr.val, clock, ptr))
            clock += 1
        return main_head.next
# Time Complexity: O(MlogK)
# Space Complexity: O(K)
# Where K is len(lists) and M is total number of nodes in lists