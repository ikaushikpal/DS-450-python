from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        prevComplete = 0
        maxTime, idE = float('-inf'), -1
        for i, leaveTime in logs:
            duration = leaveTime - prevComplete
            if duration > maxTime:
                maxTime = duration
                idE = i
            prevComplete = leaveTime
        return idE

print(Solution().hardestWorker(n = 10, logs = [[0,3],[2,5],[0,9],[1,15]]))