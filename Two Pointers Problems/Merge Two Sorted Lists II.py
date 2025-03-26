import heapq


class Solution:
	# @param A : list of integers
	# @param B : list of integers
    def merge(self, A, B):
        C = list(heapq.merge(A, B))        
        A.clear()
        
        for val in C:
            A.append(val)