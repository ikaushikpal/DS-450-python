# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.
 
# Example 1:

# Input: s = "abcde", goal = "cdeab"
# Output: true

# Example 2:

# Input: s = "abcde", goal = "abced"
# Output: false


class ZAlgorithm:
    def buildZArray(self, concatedString):
        z = [0] * len(concatedString)
        left = right = 0
        
        for i in range(1, len(concatedString)):
            if right < i:
                left = right = i
                
                while right < len(concatedString) and concatedString[right] == concatedString[right - left]:
                    right += 1
                    
                z[i] = right - left
                right -= 1
            
            else:
                k = i - left
                if z[k] < right - i + 1:
                    z[i] = z[k]
                    
                else:
                    left = i
                    while right < len(concatedString) and concatedString[right] == concatedString[right - left]:
                        right += 1
                        
                    z[i] = right - left
                    right -= 1
            
        return z
    
    def search(self, string, pattern):
        concatedString = pattern + '$' + string
        z = self.buildZArray(concatedString)

        for i in range(len(pattern), len(concatedString)):
            if z[i] == len(pattern):
                return i - len(pattern) - 1
        return -1
        

class Solution:
    def __init__(self):
        self.zAlgo = ZAlgorithm()
        
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        if not s:
            return True
        
        specialStr = f"{s}{s}"
        if self.zAlgo.search(specialStr, goal) != -1:
            return True
        else:
            return False
        