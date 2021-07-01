class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        A.sort()

        i = j = 0
        countSum = 0
        count = -1

        while i<n and j<n:
            while i<n and countSum >= B:
                countSum -= A[i]
                i += 1

            while j<n and countSum<B:
                if A[j] < B:
                    count += 1
                
                countSum += A[j]
                j += 1

                if countSum < B:
                    count += 1
        
        if count == -1:
            return 0
        return count




if __name__ == '__main__':
    arr = [1, 11, 2, 3, 15]
    B = 10
    print(Solution().solve(arr, B))
