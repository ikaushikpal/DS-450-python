from typing import List


from collections import Counter


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        self.words = words
        self.total_char = Counter(letters)
        self.score_table = score
        self.maxScore = 0
        
        self.maxScoreWordsUtil(Counter(), 0)

        return self.maxScore

    def calculateScore(self, current_chars):
        score = 0
        for key, value in current_chars.items():
            score += self.score_table[ord(key) - ord('a')] * value
        return score

    def buildNewCharSet(self, current_chars, word):
        new_current_chars = current_chars + Counter(word)

        for key in new_current_chars:
            if key not in self.total_char:
                return None

            if new_current_chars[key] > self.total_char[key]:
                return None

        return new_current_chars

    def maxScoreWordsUtil(self, current_chars, index):
        if current_chars is None:
            return

        if index >= len(self.words):
            self.maxScore = max(self.maxScore, self.calculateScore(current_chars))
            return
        
        word = self.words[index]

        # add current word
        new_current_chars = self.buildNewCharSet(current_chars, word)

        self.maxScoreWordsUtil(new_current_chars, index + 1)
        self.maxScoreWordsUtil(current_chars, index + 1)
        


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxScoreWords(words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]))

        