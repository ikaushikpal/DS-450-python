# You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

# The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

# You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

# Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

 

# Example 1:
# Input: bombs = [[2,1,3],[6,1,4]]
# Output: 2
# Explanation:
# The above figure shows the positions and ranges of the 2 bombs.
# If we detonate the left bomb, the right bomb will not be affected.
# But if we detonate the right bomb, both bombs will be detonated.
# So the maximum bombs that can be detonated is max(1, 2) = 2.


# Example 2:
# Input: bombs = [[1,1,5],[10,10,5]]
# Output: 1
# Explanation:
# Detonating either bomb will not detonate the other bomb, so the maximum number of bombs that can be detonated is 1.


# Example 3:
# Input: bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
# Output: 5
# Explanation:
# The best bomb to detonate is bomb 0 because:
# - Bomb 0 detonates bombs 1 and 2. The red circle denotes the range of bomb 0.
# - Bomb 2 detonates bomb 3. The blue circle denotes the range of bomb 2.
# - Bomb 3 detonates bomb 4. The green circle denotes the range of bomb 3.
# Thus all 5 bombs are detonated.


from collections import defaultdict
from math import sqrt
from typing import List


class Solution:
    def dist(self, x1, y1, x2, y2):
        return sqrt((x1-x2)**2 + (y1-y2)**2)
    
    def dfs(self, graph, visited, node):
        visited.add(node)
        ans = 1

        for nei in graph[node]:
            if nei in visited:
                continue
            ans += self.dfs(graph, visited, nei)
        return ans
    
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        N = len(bombs)
        graph = defaultdict(list)

        for i in range(N):
            x1, y1, r1 = bombs[i]
            
            for j in range(i+1, N):
                x2, y2, r2 = bombs[j]

                if self.dist(x1, y1, x2, y2) <= r1:
                    graph[i].append(j)

                if self.dist(x1, y1, x2, y2) <= r2:
                    graph[j].append(i)

        ans = 0
        for i in range(N):
            ans = max(ans, self.dfs(graph, set(), i))
        return ans
# Time Complexity: O(N^3)
# Space Complexity: O(N^2)


if __name__ == '__main__':
    sol =  Solution()
    print(sol.maximumDetonation([[2,1,3],[6,1,4]]))
    print(sol.maximumDetonation([[1,1,5],[10,10,5]]))
    print(sol.maximumDetonation([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))