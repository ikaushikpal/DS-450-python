class Solution:
    def minimizeResult(self, expression: str) -> str:
        left, right = expression.split('+')
        minRes = int(left) + int(right)
        ansStr = f'({left}+{right})'
        
        # trying fiding left
        for i in range(1, len(left)):
            val = int(left[:i]) * (int(left[i:]) + int(right))
            if val < minRes:
                ansStr = f'{left[:i]}({left[i:]}+{right})'
                minRes = val
        
        # trying right
        for i in range(1, len(right)):
            val = (int(left) + int(right[:i])) * int(right[i:])
            if val < minRes:
                ansStr = f'({left}+{right[:i]}){right[i:]}'
                minRes = val
        
        # finding cross
        for i in range(1, len(left)):
            for j in range(1, len(right)):
                val = int(left[:i]) * (int(left[i:]) + int(right[:j])) * int(right[j:])
                if val < minRes:
                    ansStr = f'{left[:i]}({left[i:]}+{right[:j]}){right[j:]}'
                    minRes = val
        
        return ansStr


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimizeResult("99999999+9"))