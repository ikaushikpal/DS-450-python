from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        N = len(words)
        VOWEL = 'aeiou'

        dp = [0] * N
        for i in range(N):
            dp[i] += dp[i - 1]

            if words[i][0] in VOWEL and words[i][-1] in VOWEL:
                dp[i] += 1 
        
        ans = []
        for l, r in queries:
            if l - 1 < 0:
                ans.append(dp[r])
            else:
                ans.append(dp[r] - dp[l - 1])
        return ans