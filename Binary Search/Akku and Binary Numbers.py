# Akku likes binary numbers and she likes playing with these numbers. Her teacher once gave her a question.For given value of  L and R, Akku have to find the count of number X, which have only three-set bits in it's binary representation such that "L ≤ X ≤ R".Akku is genius, she solved the problem easily. Can you do it ??


# Example 1:
# Input:
# L = 11 and R = 19 
# Output: 4
# Explanation:
# There are 4 such numbers with 3 set bits in 
# range 11 to 19.
# 11 -> 1011
# 13 -> 1101
# 14 -> 1110
# 19 -> 10011
 

# Example 2:
# Input:
# L = 25 and R = 29
# Output: 3
# Explanation:
# There are 3 such numbers with 3 set bits in
# range 25 to 29. 
# 25 -> 11001 
# 26 -> 11010 
# 28 -> 11100
from math import ceil, log
from bisect import bisect_left, bisect_right


class Solution:
    def __init__(self):
        self.allPairs = []
        
    def precompute(self):
        # first computing all number that can be represented by 3 set bits
        # and storing them to array and later sorting it
        
        for i in range(63):
            for j in range(i+1, 63):
                for k in range(j+1, 63):
                    num = (1 << i) + (1 << j) + (1 << k)
                    self.allPairs.append(num)
        self.allPairs.sort()
        
    def solve (self, L, R):
        # find lower bound for L and R ans store into left and right
        # If last element is not equal to R then just decrement right
        # now we got the range right - left + 1
        
        left = bisect_left(self.allPairs, L)
        right = bisect_right(self.allPairs, R) - 1
        
        if self.allPairs[right] > R:
            right -= 1
        
        return right - left + 1
# Time Complexity: O(63^3) + O(log(R-L))
# Space Complexity: O(63^3)


if __name__ == '__main__':
    sol = Solution()
    sol.precompute()
    print(sol.solve(11, 19))
    print(sol.solve(25, 29))
    