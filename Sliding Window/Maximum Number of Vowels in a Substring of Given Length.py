# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 
# Example 1:
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:


# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.


# Example 3:
# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # marking vowels are 1 and rest 0
        vowels = set(('a', 'e', 'i', 'o', 'u'))
        # initializing max_vowels, current_vowels to 0
        i = j = max_vowels = current_vowels = 0

        while j < len(s):
            if s[j] in vowels:
                current_vowels += 1
            
            while j - i + 1 > k:
                if s[i] in vowels:
                    current_vowels -= 1
                i += 1
            
            max_vowels = max(max_vowels, current_vowels)

            if max_vowels == k:
                return max_vowels
            
            j += 1
        return max_vowels
# Time Complexity : O(N)
# Space Complexity : O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxVowels("abciiidef", 3))
    print(sol.maxVowels("aeiou", 2))
    print(sol.maxVowels("leetcode", 3))
