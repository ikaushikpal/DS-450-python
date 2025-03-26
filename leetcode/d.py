class Solution:
    keyPad = {'2':'a',
            '22': 'b',
            '222':'c',
            '3': 'd',
            '33': 'e',
            '333':'f',
            '4': 'g',
            '44': 'h',
            '444':'i',
            '5': 'j',
            '55': 'k',
            '555':'l',
            '6': 'm',
            '66': 'n',
            '666':'o',
            '7': 'p',
            '77': 'q',
            '777':'r',
            '7777': 's',
            '8': 't',
            '88': 'u',
            '888':'v',
            '9': 'w',
            '99': 'x',
            '999':'y',
            '9999':'z'}

    def dfs(self, inputString):
        if len(inputString) == 0:
            self.count += 1
            return
        
        for i in range(min(len(inputString), 4)):
            if inputString[:i+1] in self.keyPad:
                self.dfs(inputString[i+1:])
            else:
                break

    def countTexts(self, pressedKeys: str) -> int:
        self.count = 0
        self.dfs(pressedKeys)
        return self.count % 1000000007


print(Solution().countTexts('2222233'))
# print(Solution().countTexts('222222222222222222222222222222222222'))