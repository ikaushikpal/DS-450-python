# Given a number N. The task is to reduce the given number N to 1 in the minimum number of steps. You can perform any one of the below operations in each step.

# Operation 1: If the number is even then you can divide the number by 2.
# Operation 2: If the number is odd then you are allowed to perform either (n+1) or (n-1).
# You need to print the minimum number of steps required to reduce the number N to 1 by performing the above operations.

# Examples:  

# Input : n = 15
# Output : 5
#  15 is odd 15+1=16    
#  16 is even 16/2=8     
#  8  is even 8/2=4 
#  4  is even 4/2=2     
#  2  is even 2/2=1     

# Input : n = 7
# Output : 4
#     7->6    
#     6->3 
#     3->2    
#     2->1
# There is one more way to get in 4 steps :
# 7->8,  8->4,  4->2,  2->1


class Solution:
    def countways(self, n:int) -> int:
        ans = 0

        while n:
            if n % 2 == 0:
                n = n >> 1
            elif n % 4 == 1:
                n = n - 1
            elif n % 4 == 3:
                n = n + 1
            ans += 1
        return ans
# Time Complexity: O(logN)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countways(15))
    print(sol.countways(7))