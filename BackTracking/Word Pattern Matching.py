from sympy import re


class Solution:
    def wordPatternMatching(self, pattern, word):
        self.pattern = pattern
        self.wordPatternMatchingHelper(pattern, word, {})
        print('=' * 10)

    def printResult(self, currentDict):
        for i, s in enumerate(self.pattern):
            if i == len(self.pattern)-1:
                print(currentDict[s])
            else:
                print(currentDict[s], end='-')

    def wordPatternMatchingHelper(self, remainingPattern, remainingWord, currentDict):
        if len(remainingPattern) == 0 and len(remainingWord) == 0:
            self.printResult(currentDict)
            return
        
        if len(remainingPattern) == 0 or len(remainingWord) == 0:
            return

        currentChar = remainingPattern[0]
        if currentChar in currentDict:
            pat = currentDict[currentChar]
            if len(remainingWord) >= len(pat) and pat == remainingWord[:len(pat)]:
                self.wordPatternMatchingHelper(remainingPattern[1:], remainingWord[len(pat):], currentDict)
            else:
                return
        else:
            for i in range(1, len(remainingWord) + 1):

                if remainingWord[:i] in currentDict.values():
                    continue

                currentDict[currentChar] = remainingWord[:i]
                self.wordPatternMatchingHelper(remainingPattern[1:], remainingWord[i:], currentDict)
                currentDict.pop(currentChar)


if __name__ == '__main__':
    sol = Solution()
    sol.wordPatternMatching("aba", "zzyzz")
    sol.wordPatternMatching('abcb', 'mzaddytzaddy')
    sol.wordPatternMatching('pep', 'graphtreegraph')