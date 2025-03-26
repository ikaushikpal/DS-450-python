# Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

 

# Example 1:

# Input: s = "00110110", k = 2
# Output: true
# Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
# Example 2:

# Input: s = "0110", k = 1
# Output: true
# Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 
# Example 3:

# Input: s = "0110", k = 2
# Output: false
# Explanation: The binary code "00" is of length 2 and does not exist in the array.



class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        
        bits = [False] * (1 << k)
        val = found = 0

        for i in range(k):
            val = (val << 1) + int(s[i])
        
        for i in range(k, len(s)):
            if not bits[val]:
                bits[val] = True
                found += 1

            if found == len(bits):
                return True

            val = (val << 1) - (int(s[i-k]) << k) + int(s[i])

        if not bits[val]:
            bits[val] = True
            found += 1
        return found == len(bits)



print(Solution().hasAllCodes(s = "00110110", k = 2))
print(Solution().hasAllCodes(s = "0110", k = 1))
print(Solution().hasAllCodes(s = "0110", k = 2))
print(Solution().hasAllCodes("00110", 2))
print(Solution().hasAllCodes("0000000001011100", 4))