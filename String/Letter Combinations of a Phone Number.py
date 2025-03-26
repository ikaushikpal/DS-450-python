class Solution:
    keypad = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def letterCombinations(self, digits: str):
        if len(digits) == 0:
            return []

        if len(digits) == 1:
            return [char for char in self.keypad[digits[0]]]
        
        output = self.letterCombinations(digits[1:])
        current_key = self.keypad[digits[0]]
        result = []

        for c in current_key:
            result += [c + s for s in output]

        return result



if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('678'))
        