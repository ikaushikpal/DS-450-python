from typing import List


from collections import Counter

class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        wordDict = Counter(words)

        def dfs(s):
            if len(s) == 0:
                return True
            
            for i in range(1, len(s)+1):
                if s[:i] in wordDict:
                    if dfs(s[i:]):
                        return True

            return False

        
        return dfs(s)


if __name__ == '__main__':
    sol = Solution()
    print(sol.wordBreak('leetcode', ['leet', 'code']))