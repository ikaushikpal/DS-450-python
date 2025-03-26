from typing import List


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(score), len(score[0])
        
        t = []
        for i in range(M):
            t.append((score[i][k], i))
        t.sort(reverse=True)

        ans = []
        for temp, i in t:
            ans.append(score[i])
        return ans