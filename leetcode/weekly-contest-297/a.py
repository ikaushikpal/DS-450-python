from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        if income == 0:
            return 0

        moneyLeft = income - min(income, brackets[0][0])
        tax = min(income, brackets[0][0]) * brackets[0][1] / 100

        for i in range(1, len(brackets)):
            if moneyLeft == 0:
                break
            
            rangeAmt = brackets[i][0] - brackets[i-1][0]
            amt = min(moneyLeft, rangeAmt)
            tax += amt * brackets[i][1] / 100
            moneyLeft -= amt  
        
        return tax


if __name__ == '__main__':
    sol = Solution()
    print(sol.calculateTax(brackets = [[3,50],[7,10],[12,25]], income = 10))
    print(sol.calculateTax([[1,0],[4,25],[5,50]], income = 2))
    print(sol.calculateTax(brackets = [[2,50]], income = 0))