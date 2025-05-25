# You are given a string array words and a binary array groups both of length n.

# A subsequence of words is alternating if for any two consecutive strings in the sequence, their corresponding elements at the same indices in groups are different (that is, there cannot be consecutive 0 or 1).

# Your task is to select the longest alternating subsequence from words.

# Return the selected subsequence. If there are multiple answers, return any of them.

# Note: The elements in words are distinct.

# Example 1:
# Input: words = ["e","a","b"], groups = [0,0,1]
# Output: ["e","b"]
# Explanation: A subsequence that can be selected is ["e","b"] because groups[0] != groups[2]. Another subsequence that can be selected is ["a","b"] because groups[1] != groups[2]. It can be demonstrated that the length of the longest subsequence of indices that satisfies the condition is 2.

# Example 2:
# Input: words = ["a","b","c","d"], groups = [1,0,1,1]
# Output: ["a","b","c"]
# Explanation: A subsequence that can be selected is ["a","b","c"] because groups[0] != groups[1] and groups[1] != groups[2]. Another subsequence that can be selected is ["a","b","d"] because groups[0] != groups[1] and groups[1] != groups[3]. It can be shown that the length of the longest subsequence of indices that satisfies the condition is 3.


# Constraints:
# 1 <= n == words.length == groups.length <= 100
# 1 <= words[i].length <= 10
# groups[i] is either 0 or 1.
# words consists of distinct strings.
# words[i] consists of lowercase English letters.


from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = []
        lastGroup = -1

        for i in range(len(words)):
            if groups[i] == lastGroup:
                continue
            
            ans.append(words[i])
            lastGroup = groups[i]
        return ans
# Time Complexity: O(N)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.getLongestSubsequence(words = ["e","a","b"], groups = [0,0,1]))
    print(sol.getLongestSubsequence(words = ["a","b","c","d"], groups = [1,0,1,1]))