class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        myDict = {}
        for val in A:
            if val not in myDict:
                myDict[val] = 1
            else:
                myDict[val] += 1
        
        del A[:]

        for key in sorted(myDict.keys()):
            i = 0

            while i < 2 and myDict[key] > 0:
                A.append(key)
                i += 1
                myDict[key] -= 1

        return len(A)