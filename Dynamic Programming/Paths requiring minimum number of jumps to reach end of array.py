# Given an array arr[], where each element represents the maximum number of steps that can be made forward from that element, the task is to print all possible paths that require the minimum number of jumps to reach the end of the given array starting from the first array element.

# Note: If an element is 0, then there are no moves allowed from that element.

# Examples:

# Input: arr[] = {1, 1, 1, 1, 1}
# Output:
# 0 ⇾ 1 ⇾ 2 ⇾ 3 ⇾4
# Explanation:
# In every step, only one jump is allowed.
# Therefore, only one possible path exists to reach end of the array.

# Input: arr[] = {3, 3, 0, 2, 1, 2, 4, 2, 0, 0}
# Output:
# 0 ⇾ 3 ⇾ 5 ⇾ 6 ⇾ 9
# 0 ⇾ 3 ⇾ 5 ⇾ 7 ⇾ 9


from collections import deque
from typing import List


class Solution:
    def printMinJumps(self, jumps: List[int]) -> List[str]:
        N = len(jumps)
        dp = [float('inf')] * N
        dp[-1] = 0
        
        # simple stair case with variable jumps 
        for i in range(N-2, -1, -1):
            if jumps[i] == 0:
                continue

            for j in range(i+1, min(jumps[i]+i+1, N), 1):
                dp[i] = min(dp[i], dp[j]+1)
        
        # can not reach to end of array
        if dp[0] == float('inf'):
            return []

        paths = deque([(0, dp[0], '0')])
        # format : (index, current cost, path)

        ans = []
        while paths:
            index, cost, path = paths.popleft()
            if index == N-1:
                ans.append(path)
                continue

            for j in range(index+1, min(jumps[i]+index+1, N), 1):
                if dp[j] + 1 == cost:
                    paths.append((j, dp[j], f'{path}->{j}'))
        
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.printMinJumps([1, 1, 1, 1, 1]))
    print(sol.printMinJumps([3, 3, 0, 2, 1, 2, 4, 2, 0, 0]))
        