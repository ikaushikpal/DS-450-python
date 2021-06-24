class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, a):
        res = []
        m = n = a-1

        for i in range(2*a-1):
            row = []
            for j in range(2*a-1):
                val = 1 + max(abs(m-i), abs(n-j))
                row.append(val)            
            res.append(row)

        return res

s = Solution()
print(s.prettyPrint(4))