class Solution:
    def power(self, base, exponent):
        res = self.power_util(base, exponent)

        if exponent%2:
            return res * base
        
        return res

    
    def power_util(self, base, exponent):
        if exponent == 0:
            return 1

        if exponent == 1:
            return base
            
        p = self.power_util(base, exponent // 2)
        return p * p


if __name__ == '__main__':
    sol = Solution()
    print(sol.power(2, 10))
    print(sol.power(2, 0))
    print(sol.power(3, 5))
