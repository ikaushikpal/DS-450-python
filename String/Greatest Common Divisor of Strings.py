# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



# Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"


# Example 2:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"


# Example 3:
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""


class Solution:
    def gcd(self, x, y):
        if y == 0:
            return x
        return self.gcd(y, x%y)
    
    def checkIfGcd(self, s1, s2):
        return s1 + s2 == s2 + s1
    
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not self.checkIfGcd(str1, str2):
            return ''
        
        x = self.gcd(len(str1), len(str2))
        return str1[ : x]
# Time Complexity: O(N)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.gcdOfStrings("ABCABC", "ABC"))
    print(sol.gcdOfStrings("ABABAB", "ABAB"))
    print(sol.gcdOfStrings("LEET", "CODE"))