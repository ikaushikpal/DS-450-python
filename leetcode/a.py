class Solution:
    def largestGoodInteger(self, num: str) -> str:
        outputString, valEq = '', float('-inf')

        for j in range(len(num)):
            if j >= 2 and num[j] == num[j-2]:
                value = int(num[j-2: j+1])
                if value > valEq:
                    valEq = value
                    outputString = num[j-2: j+1]
        
        return outputString

print(Solution().largestGoodInteger('6777133339'))
print(Solution().largestGoodInteger('2300019'))
print(Solution().largestGoodInteger('42352338'))
