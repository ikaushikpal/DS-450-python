# Geek just learned about Fibonacci numbers.

# The Fibonacci Sequence is the series of numbers: 0, 1, 1, 2, 3, 5, 8, 13, ...
# where the next number is found by adding up the two numbers before it.

# He defines a new series called Geeky numbers. Here the next number is the sum of the K preceding numbers.
# You are given an array of size K, GeekNum[ ], where the ith element of the array represents the ith Geeky number. Return its Nth term.

# Note: This problem can be solved in O(N2) time complexity but the user has to solve this in O(N). The Constraints are less because there can be integer overflow in the terms.


# Example 1:
# Input:
# N = 6, K = 1
# GeekNum[] = {4}
# Output: 
# 4
# Explanation: 
# Terms are 4, 4, 4, 4, 4, 4


# Example 2:
# Input:
# N = 5, K = 3
# GeekNum[] = {0, 1, 2}
# Output: 
# 6
# Explanation: 
# Terms are 0, 1, 2, 3, 6.
# So the 5th term is 6


from collections import deque


class Solution():
    def solve(self, N, K, GeekNum):
        if K >= N:
            return GeekNum[N - 1]
            
        window = deque(GeekNum)
        total = sum(GeekNum)
        
        for _ in range(N - K):
            newElement = total

            total -= window.popleft()
            window.append(newElement)
            total += newElement

        return window.pop()
# Time Complexity: O(N-K + 2K) = O(N + K)
# Space Complexity: O(K)


if __name__ == '__main__':
    sol = Solution()
    print(sol.solve(6, 1, [4]))
    print(sol.solve(5, 3, [0, 1, 2]))
