class Solution:
    def modify_string(self, s):
        newS = ''

        for char in s:
            if char.isalpha():
                newS += char
                continue
            
            if char in 'aeiou':
                newS += char.upper()
            elif char == 'z':
                newS += 'a'
            else:
                newS += chr(ord(char) + 1)

        return newS