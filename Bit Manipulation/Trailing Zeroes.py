class Solution:
    def solve(self, num):
        counter = 0
        while num:
            if num & 1 == 1:
                break
            counter += 1
            num = num >> 1
        
        return counter



s = Solution()
print(s.solve(18))