# Given a height h, count the maximum number of balanced binary trees possible with height h. Print the result modulo 109 + 7.
# Note : A balanced binary tree is one in which for every node, the difference between heights of left and right subtree is not more than 1.


# Example 1:
# Input: h = 2
# Output: 3 
# Explanation: The maximum number of balanced 
# binary trees possible with height 2 is 3. 

# Example 2:
# Input: h = 3
# Output: 15
# Explanation: The maximum number of balanced
# binary trees possible with height 3 is 15. 


class Solution:
    def helper(self, n):
        if n <= 1:
            return 1
            
        if n in self.memo:
            return self.memo[n]
        
        p1 = self.helper(n-1) ** 2
        p2 = self.helper(n-2) * self.helper(n-1)
        self.memo[n] = (p1 + 2 * p2) % 1000000007
        return self.memo[n]

    def countBT (self, h):
        self.memo = {}
        return self.helper(h)

if __name__ == '__main__':
    s = Solution()
    print(s.countBT(2))
    print(s.countBT(3))