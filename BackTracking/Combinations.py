# Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

# You may return the answer in any order.

 

# Example 1:
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]


# Example 2:
# Input: n = 1, k = 1
# Output: [[1]]


from typing import List


class Solution:
    def helper(self, i, n, k, currentCombi):
        if len(currentCombi) == k:
            self.ans.append(currentCombi[:])
            return
        
        for j in range(i+1, n+1):
            currentCombi.append(j)
            self.helper(j, n, k, currentCombi)
            currentCombi.pop()
            
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.helper(0, n, k, [])
        return self.ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.combine(4, 2))
    print(sol.combine(1, 1))