# A string s is called happy if it satisfies the following conditions:

# s only contains the letters 'a', 'b', and 'c'.
# s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# s contains at most a occurrences of the letter 'a'.
# s contains at most b occurrences of the letter 'b'.
# s contains at most c occurrences of the letter 'c'.
# Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.

# Example 2:

# Input: a = 7, b = 1, c = 0
# Output: "aabaa"
# Explanation: It is the only correct answer in this case.


import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        minHeap = [(-x, chr(char))for char, x in enumerate((a, b, c), 97) if x > 0]
        heapq.heapify(minHeap)
        output = []
        
        while minHeap:
            freq, char = heapq.heappop(minHeap)
            
            if len(output) < 2 or not (output[-1] == output[-2] == char):
                output.append(char)
                if freq < -1:
                    heapq.heappush(minHeap, (freq + 1, char))
                    
            elif minHeap:
                newFreq, newChar = heapq.heappop(minHeap)
                output.append(newChar)
                if newFreq < -1:
                    heapq.heappush(minHeap, (newFreq + 1, newChar))
                heapq.heappush(minHeap, (freq, char))
            else:
                break
        
        return ''.join(output)


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestDiverseString(1, 1, 7))