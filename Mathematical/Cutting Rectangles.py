# Given a rectangle of dimensions L x B find the minimum number (N) of identical squares of maximum side that can be cut out from that rectangle so that no residue remains in the rectangle. Also find the dimension K of that square.


# Example 1:
# Input: L = 2, B = 4
# Output: N = 2, K = 2
# Explaination: 2 squares of 2x2 dimension.


# Example 2:
# Input: L = 6, B = 3
# Output: N = 2, K = 3
# Explaintion: 2 squares of 3x3 dimension. 


class Solution:
    def gcd(self, x, y):
        if x == 0:
            return y
        return self.gcd(y%x, x)
        
    def minimumSquares(self, L, B):
        K = self.gcd(L, B)
        N = (L * B) // (K * K)
        return (N, K)
# Time Complexity: O(log(min(L, B)))
# Space Complexity: O(1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumSquares(2, 4))
    print(sol.minimumSquares(6, 3))