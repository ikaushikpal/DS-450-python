# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.


# Example 1:
# Input: s = "aab"
# Output: "aba"


# Example 2:
# Input: s = "aaab"
# Output: ""


import heapq
from collections import Counter


class Solution:
    def insertHeap(self, maxHeap, char, freq):
        if freq < -1:
            heapq.heappush(maxHeap, (freq + 1, char))

    def reorganizeString(self, s: str) -> str:
        freqMap = Counter(s)
        maxHeap = [(-value, key) for key, value in freqMap.items()]
        heapq.heapify(maxHeap)
        outputString = ''
        
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            
            if outputString and outputString[-1] == char:
                if not maxHeap:
                    return '' 
                
                otherFreq, otherChar = heapq.heappop(maxHeap)
                outputString += otherChar
                self.insertHeap(maxHeap, otherChar, otherFreq)
            
            outputString += char
            self.insertHeap(maxHeap, char, freq)
        return outputString
# Time Complexity: O(NlogN)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.reorganizeString("aab"))
    print(sol.reorganizeString("aaab"))
    print(sol.reorganizeString("a"))