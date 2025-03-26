# Given a string S consisting of uppercase and lowercase characters. The task is to sort uppercase and lowercase letters separately such that if the ith place in the original string had an Uppercase character then it should not have a lowercase character after being sorted and vice versa.


# Example 1:
# Input:
# N = 12
# S = defRTSersUXI
# Output: deeIRSfrsTUX
# Explanation: Sorted form of given string
# with the same case of character as that
# in original string is deeIRSfrsTUX


# Example 2:
# Input:
# N = 6
# S = srbDKi
# Output: birDKs
# Explanation: Sorted form of given string
# with the same case of character will
# result in output as birDKs.


class Solution:
    def countSort(self, chars):
        freq = [0] * 128
        for char in chars:
            freq[ord(char)] += 1
        
        newChars = []
        for i in range(128):
            while freq[i] > 0:
                newChars.append(chr(i))
                freq[i] -= 1
        return newChars
        
    #Function to perform case-specific sorting of strings.
    def caseSort(self, s, n):
        lower = [char for char in s if char.islower()]
        upper = [char for char in s if char.isupper()]
        
        lower = self.countSort(lower)
        upper = self.countSort(upper)
        
        newS = ''
        i = j = 0
        for char in s:
            if char.islower():
                newS += lower[i]
                i += 1
            else:
                newS += upper[j]
                j += 1
        return newS

# Time Complexity: O(4*N) = O(N)
# Space Complexity: O(N + 128) = O(N) 


if __name__ == '__main__':
    sol = Solution()
    print(sol.caseSort('defRTSersUXI', 12))
    print(sol.caseSort('srbDKi', 6))