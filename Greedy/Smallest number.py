# The task is to find the smallest number with given sum of digits as S and number of digits as D.

 
# Example 1:
# Input:
# S = 9 
# D = 2
# Output:
# 18
# Explanation:
# 18 is the smallest number
# possible with sum = 9
# and total digits = 2.
 

# Example 2:
# Input:
# S = 20
# D = 3
# Output:
# 299
# Explanation:
# 299 is the smallest number
# possible with sum = 20
# and total digits = 3.


class Solution:
    def smallestNumber (self, S, D):
        if 9 * D < S:
            return -1
        
        num = ''
        for i in range(D-1, -1, -1):
            if S > 9:
                num += '9'
                S -= 9
            else:
                if i == 0:
                    num += str(S)
                else:
                    num += str(S - 1)
                    num += '0' * max(0, i - 1)
                    num += '1'
                    break
        return num[::-1]
# Time Complexity: O(D)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.smallestNumber(9, 2))
    print(sol.smallestNumber(20, 3))