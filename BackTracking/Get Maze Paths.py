from functools import lru_cache
from time import time


class Solution:
    # @lru_cache(maxsize=12, typed=False)
    def get_maze_helper(self, current_x, current_y, rows, cols, path):
        if current_x == rows and current_y == cols:
            self.result.append(path)
            return

        if current_x > rows or current_y > cols:
            return

        self.get_maze_helper(current_x, current_y + 1, rows, cols, path + 'h')
        self.get_maze_helper(current_x + 1, current_y, rows, cols, path + 'v')

    def get_maze(self, rows:int, cols:int):
        self.result = []
        self.get_maze_helper(0, 0, rows-1, cols-1, '')
        return self.result


if __name__ == '__main__':
    s = Solution()
    print(s.get_maze(10, 10))
