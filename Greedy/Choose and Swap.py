class Solution:
    def chooseandswap (self, string):
        occurrences = {}
    
        for i in range(len(string)):
            char = string[i]
            if char not in occurrences:
                occurrences[char] = i

        for i in range(len(string)):
            char = string[i]
            
            if char not in occurrences:
                continue
            
            occurrences.pop(char)
    
            if len(occurrences) == 0:
                return string
            
            minChar = min(occurrences, key=lambda x: x)
            minChar = occurrences[minChar]

            if i < minChar and ord(string[minChar]) < ord(char):
                rChar = string[minChar]
                res = ''
                
                for j in range(len(string)):
                    xChar = string[j]

                    if xChar == char:
                        res += rChar

                    elif xChar == rChar:
                        res += char

                    else:
                        res += xChar
                return res
            
        return string


if __name__ == '__main__':
    sol = Solution()
    print(sol.chooseandswap('abba'))