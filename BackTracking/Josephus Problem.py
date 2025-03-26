class Solution:
    def josephus_problem(self, n:int, k:int):
        if n == 1:
            return 0
        
        x = self.josephus_problem(n-1, k)
        return (x + k) % n


if __name__ == '__main__':
    sol = Solution()
    print(sol.josephus_problem(6, 3))