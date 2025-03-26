# Given a number (n) and no. of digits (m) to represent the number, we have to check if we can represent n using exactly m digits in any base from 2 to 32.



# Example 1:
# Input: n = 8, m = 2
# Output: Yes 
# Explanation: Possible in base 3 as 8 in base 3 is 22.  


# Example 2:
# Input: n = 8, m = 3
# Output: No
# Explanation: Not possible in any base. 


from math import log, floor


class Solution:
    def countDigit(self, n, base):
        return floor(log(n) / log(base)) + 1
        
    def baseEquiv(self, n, m):
        low, high = 2, 32

        while low <= high:
            mid = (low + high) >> 1
            temp = self.countDigit(n, mid)

            if temp == m:
                return 'Yes'
            elif temp > m:
                low = mid + 1
            else:
                high = mid - 1
        return 'No'
# Time Complexity: O(32logN) = O(logN)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.baseEquiv(8, 2))
    print(sol.baseEquiv(8, 3))