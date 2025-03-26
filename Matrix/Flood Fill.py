from typing import List


class Solution:
    def __init__(self):
        self.dir_x = [-1, +1, 0, 0]
        self.dir_y = [0, 0, -1, +1]

    def check_valid(self, x ,y ):
        if 0<=x<self.row and 0<=y<self.col:
            return True
        return False

    def dfs(self, x, y):
        self.visited[x][y] = True
        current_pixel = self.image[x][y]

        for del_x, del_y in zip(self.dir_x, self.dir_y):
            new_x = x + del_x
            new_y = y + del_y

            if self.check_valid(new_x, new_y) and self.image[new_x][new_y] == current_pixel and not self.visited[new_x][new_y]:
                self.dfs(new_x, new_y)

        self.image[x][y] = self.newColor

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.row = len(image)
        self.col = len(image[0])
        self.image = image
        self.visited = [[False]*self.col for _ in range(self.row)]
        self.newColor = newColor

        self.dfs(sr, sc)

        return self.image

if __name__ == '__main__':
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2

    sol = Solution()
    print(sol.floodFill(image, sr, sc, newColor))