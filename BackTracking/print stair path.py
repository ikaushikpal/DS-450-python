class Solution:
    def print_stair_path(self, n:int) -> None:
        self.print_stair_path_util(n, '')

    def print_stair_path_util(self, n:int, current_path:str) -> None:
        if n < 0:
            return

        if n == 0:
            print(current_path)
            return
        
        for i in range(1, 4):
            self.print_stair_path_util(n-i, current_path + str(i))


if __name__ == '__main__':
    s = Solution()
    s.print_stair_path(4)
