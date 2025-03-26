class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, arr):
        if len(arr) <= 1:
            return len(arr)
        
        arr = list(set(arr))

        return len(arr)
    

if __name__ == '__main__':
    arr = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ]
    print(Solution().removeDuplicates(arr))