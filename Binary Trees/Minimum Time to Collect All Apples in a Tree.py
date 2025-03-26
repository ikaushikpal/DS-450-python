# Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.

# The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple; otherwise, it does not have any apple.

 

# Example 1:
#     0
#   /    \ 
#  1      2*
# / \     / \
# 4*  5*  3  6

# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
# Output: 8 
# Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  



# Example 2:
#     0
#   /    \ 
#  1      2*
# / \     / \
# 4  5*  3  6

# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
# Output: 6
# Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  



# Example 3:
#     0
#   /    \ 
#  1      2
# / \    / \
# 4  5   3  6
# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
# Output: 0


from typing import List
from collections import defaultdict


class Solution:
    def dfs(self, currentNode, tree, hasApple, seen) -> int:
        if currentNode in seen:
            return 0
        
        seen.add(currentNode)
        childCost = 0
        myCost = 2

        for child in tree[currentNode]:
            childCost += self.dfs(child, tree, hasApple, seen)
        
        # if no need to visit
        if childCost == 0 and hasApple[currentNode] == False:
            return 0
        
        return myCost + childCost

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = defaultdict(list)

        for parent, child in edges:
            tree[parent].append(child)
            tree[child].append(parent)

        return max(0, self.dfs(0, tree, hasApple, set())-2)



if __name__ == '__main__':
    sol = Solution()
    print(sol.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False, True,False, True, True,False]))
    print(sol.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,False,True,False]))
    print(sol.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,False,False,False,False,False]))
