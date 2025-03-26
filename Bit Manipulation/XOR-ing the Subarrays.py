class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, arr):
        res = 0
        for L in range(1, len(arr)+1):
            for i in range(0, len(arr)-L+1):
                for j in range(i, i+L):
                    index = j % len(arr)
                    res ^= arr[index]
        
        return res



sol = Solution()
print(sol.solve([4, 5, 7, 5]))

