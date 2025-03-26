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


    def countTexts(self, pressedKeys: str) -> int:
        i = j = 0
        ans = 1

        while j < len(pressedKeys):
            count = 0
            while j < len(pressedKeys) and pressedKeys[i] == pressedKeys[j]:
                count += 1
                j += 1
            
            if pressedKeys[j-1] not in ('7', '9'):
                if count > 3:
                    temp = 4
                    count -= 3
                    for _ in range(count):
                        temp = temp + temp - 1
                    ans *= temp
                else:
                    ans *= (2 ** (count - 1)) 
            else:
                if count > 4:
                    temp = 8
                    count -= 4
                    for _ in range(count):
                        temp = temp + temp - 1
                    ans *= temp
                else:
                    ans *= (2 ** (count - 1)) 
            i = j
        return ans % ((10 ** 9) + 7)

# print(Solution().countTexts('2222233'))
print(Solution().countTexts('222222222222222222222222222222222222'))