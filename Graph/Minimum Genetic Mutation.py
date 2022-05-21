# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

# Suppose we need to investigate a mutation from a gene string start to a gene string end where one mutation is defined as one single character changed in the gene string.

# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

# Given the two gene strings start and end and the gene bank bank, return the minimum number of mutations needed to mutate from start to end. If there is no such a mutation, return -1.

# Note that the starting point is assumed to be valid, so it might not be included in the bank.

 
# Example 1:
# Input: start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
# Output: 1


# Example 2:
# Input: start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
# Output: 2


# Example 3:
# Input: start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
# Output: 3


from collections import deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        allValidMutations = set(bank)
        if end not in allValidMutations:
            return -1

        queue = deque([(start, 0)])
        visited = set()
        visited.add(start)

        while queue:
            curr, level = queue.popleft()
            if curr == end:
                return level

            for i in range(len(curr)):
                for j in 'ACGT':
                    nextSeq = curr[:i] + j + curr[i+1:]
                    if nextSeq in allValidMutations and nextSeq not in visited:
                        visited.add(nextSeq)
                        queue.append((nextSeq, level + 1))

        return -1
# Time Complexity: O(4 * n * k) = O(n * k)
# Where n is the length of the start string and k is the length of the bank.


if __name__ == "__main__":
    start = "AACCGGTT"
    end = "AACCGGTA"
    bank = ["AACCGGTA"]
    print(Solution().minMutation(start, end, bank))

    start = "AACCGGTT"
    end = "AAACGGTA"
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    print(Solution().minMutation(start, end, bank))

    start = "AAAAACCC"
    end = "AACCCCCC"
    bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
    print(Solution().minMutation(start, end, bank))
