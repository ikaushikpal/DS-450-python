# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 
# Example 1:
# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1

# Example 2:
# Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
# Output: 3
 

# Constraints:
# 1 <= dominoes.length <= 4 * 10^4
# dominoes[i].length == 2
# 1 <= dominoes[i][j] <= 9


from collections import defaultdict
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freq = defaultdict(int)
        ans = 0

        for height, width in dominoes:
            original_dominoe = (height, width)
            roatated_dominoe = (width, height)

            if original_dominoe in freq:
                ans += freq[original_dominoe]
            
            if original_dominoe != roatated_dominoe and roatated_dominoe in freq:
                ans += freq[roatated_dominoe]


            freq[original_dominoe] += 1
        return ans
# Time Complexity: O(n)
# Space Complexity: O(n)


if __name__ == '__main__':
    sol = Solution()
    print(sol.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))
    print(sol.numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]]))