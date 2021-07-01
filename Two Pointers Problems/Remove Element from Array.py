class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        C = []
        for val in A:
            if val != B:
                C.append(val)

        del A[:]

        for val in C:
            A.append(val)

        return len(A)