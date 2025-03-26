# You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

# A uni-value grid is a grid where all the elements of it are equal.

# Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.


# Example 1:
# Input: grid = [[2,4],[6,8]], x = 2
# Output: 4
# Explanation: We can make every element equal to 4 by doing the following:
# - Add x to 2 once.
# - Subtract x from 6 once.
# - Subtract x from 8 twice.
# A total of 4 operations were used.

# Example 2:
# Input: grid = [[1,5],[2,3]], x = 1
# Output: 5
# Explanation: We can make every element equal to 3.

# Example 3:
# Input: grid = [[1,2],[3,4]], x = 2
# Output: -1
# Explanation: It is impossible to make every element equal.


# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 105
# 1 <= m * n <= 105
# 1 <= x, grid[i][j] <= 104


from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        M, N = len(grid), len(grid[0])
        grid_flat = []
        total = 0
        rem = grid[0][0] % x

        for i in range(M):
            for j in range(N):
                # to convert all numbers to same number then all numbers remainder has to be same
                if grid[i][j] % x != rem:
                    return -1
                total += grid[i][j]
                grid_flat.append(grid[i][j])

        # to find the min cost
        # trying all possible solution
        # using prefix sum to calculate the cost in O(1)
        grid_flat.sort()
        prefix_sum = 0
        min_cost = float("inf")

        for i, num in enumerate(grid_flat):
            # checking if want to make all elements to grid_flat[i]
            # then what will be the cost

            left_target = i * num  # left side sum should be
            right_target = (len(grid_flat) - i - 1) * num  # right side sum should be

            left_sum = prefix_sum  # actual left side sum
            right_sum = total - prefix_sum - num  # actual right side sum

            left_cost = (left_target - left_sum) // x
            right_cost = (right_sum - right_target) // x

            cost = left_cost + right_cost
            min_cost = min(min_cost, cost)

            prefix_sum += num
        return min_cost


# Time Complexity: O(M*Nlog(M*N))
# Space Complexity: O(M*N)


if __name__ == "__main__":
    sol = Solution()
    print(sol.minOperations(grid=[[2, 4], [6, 8]], x=2))
    print(sol.minOperations(grid=[[1, 5], [2, 3]], x=1))
    print(sol.minOperations(grid=[[1, 2], [3, 4]], x=2))
