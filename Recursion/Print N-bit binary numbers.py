# Print N-bit binary numbers having more 1’s than 0’s for any prefix

class Solution:
    def __init__(self):
        self.res = []
    
    def solve(self, n):
        if n==0:
            return []
        if n==1:
            return ['1']

        self.__solveUtil(1,0,'1',n-1)
        return self.res

    def __solveUtil(self, no1, no0, output_string, n):
        if no0 > no1:
            return

        if n == 0:
            if no1 >= no0:
                self.res.append(output_string)
            return
        
        self.__solveUtil(no1+1, no0, output_string + '1', n-1)
        self.__solveUtil(no1, no0+1, output_string + '0', n-1)
    

sol = Solution()
res = sol.solve(4)
print(res)