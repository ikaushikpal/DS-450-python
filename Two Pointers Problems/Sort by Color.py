class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        count0 = count1 = count2 = 0

        for val in A:
            if val == 0: count0 += 1
            elif val == 1: count1 += 1
            else: count2 += 1
        
        i = 0
        while count0 > 0:
            A[i] = 0; count0-=1; i+= 1
        while count1 > 0:
            A[i] = 1; count1-=1; i+= 1
        while count2 > 0:
            A[i] = 2; count2-=1; i+= 1
        
        return A