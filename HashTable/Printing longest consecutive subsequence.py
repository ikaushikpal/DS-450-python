class Solution:
    
    # arr[] : the input array
    # N : size of the array arr[]
    
    #Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self, arr, N):
        myDict = { val:True for val in arr }

        for ele in arr:
            if ele-1 in myDict:
                myDict[ele] = False
        
        sequence = []

        for key in myDict:
            if myDict[key] == True: # staring of new sequence
                tempSeq, val = [], key

                while val in myDict:
                    tempSeq.append(val)
                    val += 1
                
                if len(tempSeq) > len(sequence):
                    sequence = tempSeq

        return sequence


if __name__ == '__main__':
    arr = [1, 9, 3, 10, 4, 20, 2]
    print(Solution().findLongestConseqSubseq(arr, len(arr)))

    arr = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
    print(Solution().findLongestConseqSubseq(arr, len(arr)))