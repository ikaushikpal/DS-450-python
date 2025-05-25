# There is a dungeon with n x m rooms arranged as a grid.

# You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes one second for one move and two seconds for the next, alternating between the two.

# Return the minimum time to reach the room (n - 1, m - 1).

# Two rooms are adjacent if they share a common wall, either horizontally or vertically.

# Example 1:
# Input: moveTime = [[0,4],[4,4]]
# Output: 7
# Explanation:
# The minimum time required is 7 seconds.
# At time t == 4, move from room (0, 0) to room (1, 0) in one second.
# At time t == 5, move from room (1, 0) to room (1, 1) in two seconds.

# Example 2:
# Input: moveTime = [[0,0,0,0],[0,0,0,0]]
# Output: 6
# Explanation:
# The minimum time required is 6 seconds.
# At time t == 0, move from room (0, 0) to room (1, 0) in one second.
# At time t == 1, move from room (1, 0) to room (1, 1) in two seconds.
# At time t == 3, move from room (1, 1) to room (1, 2) in one second.
# At time t == 4, move from room (1, 2) to room (1, 3) in two seconds.

# Example 3:
# Input: moveTime = [[0,1],[1,2]]
# Output: 4


# Constraints:
# 2 <= n == moveTime.length <= 750
# 2 <= m == moveTime[i].length <= 750
# 0 <= moveTime[i][j] <= 10^9


import heapq
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        N, M = len(moveTime), len(moveTime[0])
        INF = float('inf')
        dp = [M * [INF] for _ in range(N)]

        min_heap = [(0, 1, 0, 0)] # (time, cost, x, y)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while min_heap:
            time, cost, x, y = heapq.heappop(min_heap)

            if time >= dp[x][y]:
                continue

            if x == N - 1 and y == M - 1:
                return time

            dp[x][y] = time
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy

                if 0 > new_x or new_x >= N:
                    continue
                
                if 0 > new_y or new_y >= M:
                    continue
                
                if dp[new_x][new_y] != INF:
                    continue
                
                new_time = max(time, moveTime[new_x][new_y]) + cost
                new_cost = 2 if cost == 1 else 1
                heapq.heappush(min_heap, (new_time, new_cost, new_x, new_y))
        return -1 
# Time Complexity: O(N * M * log(N * M))
# Space Complexity: O(N * M)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minTimeToReach([[0,4],[4,4]]))
    print(sol.minTimeToReach([[0,0,0,0],[0,0,0,0]]))
    print(sol.minTimeToReach([[0,1],[1,2]]))
