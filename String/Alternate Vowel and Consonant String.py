# Given a string S of lowercase english characters. Rearrange characters of the given string such that the vowels and consonants occupy alternate positions and the string so formed should be lexicographically (alphabetically) smallest. 
# Note: Vowels are 'a', 'e', 'i', 'o' and 'u'. 


# Example 1:
# Input:
# S = "aeroplane"
# Output: alanepero
# Explanation: alanepero  
# The vowels and consonants are arranged 
# alternatively with vowels shown in bold.
# Also, there's no lexicographically smaller
# string possible with required conditions.


# Example 2:
# Input: 
# S = "mississippi"
# Output: -1
# Explanation: The number of vowels is 4 
# whereas the number of consonants is 7.
# Hence, there's no way to arrange the
# vowels and consonants alternatively.


class Solution:
    def rearrange(self, S, N):
        vowels = [0] * 26
        consonants = [0] * 26
        countVowel = countConsonant = 0
        
        for char in S:
            if char in 'aeiou':
                vowels[ord(char) - 97] += 1
                countVowel += 1
            else:
                consonants[ord(char) - 97] += 1
                countConsonant += 1
        
        if abs(countVowel - countConsonant) >= 2:
            return '-1'
            
        ans = ''
        i = j = 0
        
        while i<26 and vowels[i] == 0:
            i += 1
        
        while j<26 and consonants[j] == 0:
            j += 1
            
        while countVowel > 0 and countConsonant > 0:
            vowel = chr(i + 97)
            consonant = chr(j + 97)
            
            if countVowel == countConsonant:
                if not ans:
                    ans += min(vowel, consonant)
                    ans += max(vowel, consonant)
                    
                elif ans[-1] in 'aeiou':
                    ans += consonant
                    ans += vowel
                    
                else:
                    ans += vowel
                    ans += consonant
                    
            elif countVowel > countConsonant:
                ans += vowel
                ans += consonant
                
            else:
                ans += consonant
                ans += vowel
                
            vowels[i] -= 1
            consonants[j] -= 1
            
            countVowel -= 1
            countConsonant -= 1
            
            while i<26 and vowels[i] == 0:
                i += 1
            
            while j<26 and consonants[j] == 0:
                j += 1
        
        if countVowel > 0:
            vowel = chr(i + 97)
            ans += vowel
        
        if countConsonant > 0:
            consonant = chr(j + 97)
            ans += consonant
        
        return ans
# Time Complexity: O(N)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.rearrange('aeroplane', 9))
