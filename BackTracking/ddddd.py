class Solution:
    def helper(self, i, n, k, currentCombi):
        if len(currentCombi) == k:
            self.ans.append(''.join(map(str, currentCombi)))
            return
        
        for j in range(i+1, n+1):
            currentCombi.append(j)
            self.helper(j, n, k, currentCombi)
            currentCombi.pop()
            
    def combine(self, n: int, k: int):
        self.ans = []
        self.helper(0, n, k, [])
        return self.ans


s = Solution()
# print(s.combine(3, 2))

from functools import reduce
from itertools import permutations




def solve(n, k):
    s = []
    def helper(n, k, curr):
        if n == 0:
            s.append(curr)
            return
        
        for i in range(k):
            helper(n-1, k, curr + str(i))

    helper(n, k, '')
    res = reduce(lambda i, j: i + j[next(idx 
            for idx in reversed(range(len(j) + 1)) 
            if i.endswith(j[:idx])):], s, '', )
    return res

print(solve(2, 2))