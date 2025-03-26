class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
    def diffPossible(self, A, B):
        i = 0
        n = len(A)
        j = 1
        while i<n and j<n:
            if A[j] - A[i] == B:
                if i == j: j+=1
                else: return 1

            elif A[j] - A[i] > B:
                i += 1
            else:
                j += 1
                
        return 0