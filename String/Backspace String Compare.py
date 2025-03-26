# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

 

# Example 1:
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".



# Example 2:
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".



# Example 3:
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".


class Solution:
    def removeExcessCharacter(self, s):
        outputString = ''
        backSpaceCount = 0
        
        for i in range(len(s)-1, -1, -1):
            if s[i] != '#':
                if backSpaceCount > 0:
                    backSpaceCount -= 1
                else:
                    outputString += s[i]
            else:
                backSpaceCount += 1
            
        return outputString[::-1]
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        sModified = self.removeExcessCharacter(s)
        tModified = self.removeExcessCharacter(t)
        
        return sModified == tModified


if __name__ == "__main__":
    sol = Solution()
    print(sol.backspaceCompare("ab#c", "ad#c"))
    print(sol.backspaceCompare("ab##", "c#d#"))
    print(sol.backspaceCompare("a#c", "b"))