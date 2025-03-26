# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 
# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true


# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false


# Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sList = s.split()
        if len(pattern) != len(sList):
            return False

        sPatternMap = {}
        patternSMap = {}

        for i in range(len(pattern)):
            if pattern[i] not in patternSMap:
                if sList[i] not in sPatternMap:
                    sPatternMap[sList[i]] = pattern[i]
                    patternSMap[pattern[i]] = sList[i]
                else:
                    return False
            else:
                if sList[i] != patternSMap[pattern[i]]:
                    return False
        return True
# Time Complexity: O(N)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.wordPattern("abba", "dog cat cat dog"))
    print(sol.wordPattern("abba", "dog cat cat fish"))
    print(sol.wordPattern("aaaa", "dog cat cat dog"))