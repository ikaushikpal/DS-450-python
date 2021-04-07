import heapq


class Solution:
    def mergeKLists(self, arr, K):
        heap = []
        counter = 0

        for node in arr:
            if node != None:
                heapq.heappush(heap, (node.data, counter, node))
            counter += 1

        if len(heap) == 0:
            return None

        main_head = last_node = None
        i = 0
        while len(heap):
            x, y, current_node = heapq.heappop(heap)
            if main_head == None:
                main_head = last_node = current_node
            else:
                last_node.next = current_node
                last_node = current_node

            next_node = current_node.next
            if next_node:
                heapq.heappush(heap, (next_node.data, counter, next_node))
            counter += 1

        return main_head
