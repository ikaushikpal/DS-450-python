from typing import List
from collections import Counter


class Solution:
    def solveQueries(self, N : int, num : int, A : List[int], Q : List[List[int]]) -> List[int]:
        eleCounter = []
        c = Counter()
        for i in range(N):
            c[A[i]] += 1
            eleCounter.append(c.copy())
        
        ans = []
        for l, r, k in Q:
            high = eleCounter[r]
            low = Counter() if l == 0 else eleCounter[l - 1]
            temp = high - low
            ans.append(temp.values().count(k))
        return ans
    

if __name__ == '__main__':
    sol = Solution()
    print(sol.solveQueries(10,
                            5,
                            [7, 4, 2, 9, 2, 5, 8, 10, 7, 10],
                            [[1, 1, 1],
                            [0, 9, 2],
                            [3, 3, 1],
                            [5, 5, 2],
                            [0, 0, 0]]))
    print(sol.solveQueries(5, 3, [1,1,3,4,3], [[0, 2, 2], [0, 2, 1], [0, 4, 2]]))