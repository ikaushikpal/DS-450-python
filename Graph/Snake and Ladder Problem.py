# https://practice.geeksforgeeks.org/problems/snake-and-ladder-problem4816/1

# Given a 5x6 snakes and ladders board, find the minimum number of dice throws required to reach the destination or last cell (30th cell) from the source (1st cell).

# You are given an integer N denoting the total number of snakes and ladders and an array arr[] of 2*N size where 2*i and (2*i + 1)th values denote the starting and ending point respectively of ith snake or ladder. The board looks like the following.


                                   

# Example 1:

# Input:
# N = 8
# arr[] = {3, 22, 5, 8, 11, 26, 20, 29, 
#        17, 4, 19, 7, 27, 1, 21, 9}

# Output: 3
# Explanation:
# The given board is the board shown
# in the figure. For the above board 
# output will be 3. 
# a) For 1st throw get a 2. 
# b) For 2nd throw get a 6.
# c) For 3rd throw get a 2.

# Your Task:
# You do not need to read input or print anything. Your task is to complete the function minThrow() which takes N and arr as input parameters and returns the minimum number of throws required to reach the end of the game.


from collections import deque


class Solution:
    def simulate(self, ROWS, COLS, snakesLadders):
        visited = set()
        targetCell = ROWS * COLS
        queue = deque([(1, 0)]) # (cell, dist)
        visited.add(1)

        while queue:
            curr, cost = queue.popleft()
            if curr == targetCell:
                return cost

            for i in range(1, 7):
                newPos = curr + i
                if newPos == targetCell:
                    return cost + 1
                
                if newPos in snakesLadders:
                    newPos = snakesLadders[newPos]
                
                if newPos not in visited:
                    visited.add(newPos)
                    queue.append((newPos, cost + 1))
        
        return -1

    def minThrow(self, N, arr):
        snakesLadders = {}
        for i in range(0, len(arr), 2):
            u, v = arr[i], arr[i+1]
            snakesLadders[u] = v

        return self.simulate(5, 6, snakesLadders) 
# Time Complexity : O(5X6 X 6) = O(N X 6) = O(N)
# space Complexity: O(5X6) = O(N)
# N is the number of board cells


if __name__ == '__main__':
    sol = Solution()
    print(sol.minThrow(8, [3, 22, 5, 8, 11, 26, 20, 29, 17, 4, 19, 7, 27, 1, 21, 9]))
    print(sol.minThrow(2, [12, 18, 3, 19]))
