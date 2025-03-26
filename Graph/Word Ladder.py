# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.


from collections import deque, defaultdict
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        nei = defaultdict(list)
        wordList.append(beginWord)
        queue = deque([beginWord])
        visited = set([beginWord])
        level = 1
        # here we are doing very clever steps
        # lets say we have a word "hot"
        # then patterns can be *ot, h*t, ho* 
        # we don't need to scan all words in wordList
        # simply check if these patterns [*ot, h*t, ho*] exists in nei
        # so now we don't need to check all words
        # only check those words which lie in those patterns

        # why this pattern thing? in problem statement its given that
        # from a word it only can go to those word which differ only by one character
        for word in wordList:
            for j in range(len(beginWord)):
                pattern = f'{word[:j]}*{word[j+1:]}'
                nei[pattern].append(word)    
        # to perform all this pattern adj list
        # time complexity is n*m

        # now doing BFS
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                
                # found destination word
                if curr == endWord:
                    return level
                
                # here we are finding patterns of curr word
                for j in range(len(curr)):
                    pattern = f'{curr[:j]}*{curr[j+1:]}'
                    # lets say pattern = 'h*t'
                    # then check those words which in 'h*t' 
                    for pat in nei[pattern]:
                        # making sure not using used words
                        if pat not in visited:
                            visited.add(pat)
                            queue.append(pat)
            level += 1
        return 0
# Time Complexity : O(n * m**2) where n is total words in wordList and m is length of each word
# Space Complexity: O(n) -> for queue
#                   O(n) -> for visited
#                   O(nm) -> for nei
#                   total = O(nm) assuming that for each word it takes O(1)


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(Solution().ladderLength(beginWord, endWord, wordList))
