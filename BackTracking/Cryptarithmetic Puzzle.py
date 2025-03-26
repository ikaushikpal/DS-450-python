from collections import Counter


class Solution:
    def buildInitialCharset(self, strings):
        self.charSet = {}
        for string in strings:
            for letter in string:
                if letter not in self.charSet:
                    self.charSet[letter] = -1

    def cryptarithmeticPuzzle(self, *strings:list):
        self.args = strings[:-1]
        self.target = strings[-1]

        self.buildInitialCharset(strings)
        if len(self.charSet) > 10:
            return 'Invalid Unique characters'
        
        self.visited = [False] * 10
        uniqueChars = ''.join(self.charSet.keys())

        self.cryptarithmeticPuzzleHelper(uniqueChars)
    
    def printCharset(self):
        for key, value in self.charSet.items():
            print(f'{key}={value}',end=' ')
        
        print()

    def computeStringSum(self, args):
        if type(args) not in (tuple, list):
            args = [args]

        totalValue = 0
        for arg in args:
            value = 0
            for letter in arg:
                value = value * 10 + self.charSet[letter]

            totalValue += value
        
        return totalValue

    def cryptarithmeticPuzzleHelper(self, uniqueChars):
        if len(uniqueChars) == 0:
            if self.computeStringSum(self.args) == self.computeStringSum(self.target):
                self.printCharset()
            return
        
        currentChar = uniqueChars[0]
        for i in range(0, 10):
            if not self.visited[i]:
                self.visited[i] = True
                self.charSet[currentChar] = i

                self.cryptarithmeticPuzzleHelper(uniqueChars[1:])

                self.visited[i] = False
                self.charSet[currentChar] = -1
        

if __name__ == '__main__':
    sol = Solution()
    sol.cryptarithmeticPuzzle('SEND', 'MORE', 'MONEY')
    print('=' * 50)
    sol.cryptarithmeticPuzzle('CP', 'IS', 'FUN')
    print('=' * 50)
    sol.cryptarithmeticPuzzle('CP', 'IS', 'FUN', 'TRUE')