# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
 
# Example 1:

# Input: n = 3
# Output: 5

#FORMULA is 2nCn/ n+1 catelon number


class Solution:
    def numTrees(self, n: int) -> int:
        res = 1
        x = 2*n
        for i in range(n):
            res = res * (x-1)
            res = res // (i+1)
        
        return res // (n+1)


if __name__ == '__main__':
    n = 3

    print(Solution().numTrees(n))
        