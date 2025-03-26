from collections import defaultdict


class Solution:
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, string:str, pattern:str) -> str:
        minWindow = len(string) + 1
        # for edge case where pattern == string

        outputString = '-1'
        patternDict = defaultdict(lambda : 0)

        for char in pattern:
            patternDict[char] += 1
    
        uniqueChars = len(patternDict)
        j = 0

        for i in range(len(string)):
            if string[i] in patternDict:
                # if string[i] exist in patternDict then
                # decrease req char count
                patternDict[string[i]] -= 1
                if patternDict[string[i]] == 0: # checking if we have enough string[i] chars for pattern
                    uniqueChars -= 1
            
            if uniqueChars == 0:
                # we found one solution
                while uniqueChars == 0:
                    # now comes to reduce
                    
                    # first store current big result
                    currentWindow = i-j+1
                    if currentWindow < minWindow:
                        minWindow = currentWindow
                        outputString = string[j : i+1]
                        
                    # just reverse of what we did above
                    if string[j] in patternDict:
                        patternDict[string[j]] += 1
                        
                        if patternDict[string[j]] >= 1:
                            uniqueChars += 1

                    j += 1

                
        if uniqueChars == 0: # for last check for edge cases
            currentWindow = i-j+1
            if currentWindow < minWindow:
                minWindow = currentWindow
                outputString = string[j : i+1]

        return outputString


if __name__ == '__main__':
    S = "timetopractice"
    P = "toc"

    print(Solution().smallestWindow(S, P))
    print(Solution().smallestWindow("zoomlazapzo", "oza"))