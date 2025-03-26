# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Follow up: Do not use any built-in library function such as sqrt.

 
# Example 1:
# Input: num = 16
# Output: true


# Example 2:
# Input: num = 14
# Output: false


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # binary search
#         low, high = 1, num
        
#         while low <= high:
#             mid = (low + high) >> 1
#             midSq = mid * mid
            
#             if midSq == num:
#                 return True
#             elif midSq < num:
#                 low = mid + 1
#             else:
#                 high = mid - 1
                
#         return False
        
        # newton ralphson
        # xn = (xn + num/xn) / 2
        # do this for sometimes and we will get our sqrt
        xn = num
        while xn * xn > num:
            xn = (xn + num/xn) // 2
        
        return xn*xn == num


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPerfectSquare(16))
    print(sol.isPerfectSquare(14))