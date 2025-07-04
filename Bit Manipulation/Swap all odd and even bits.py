# Given an unsigned integer N. The task is to swap all odd bits with even bits. For example, if the given number is 23 (00010111), it should be converted to 43(00101011). Here, every even position bit is swapped with an adjacent bit on the right side(even position bits are highlighted in the binary representation of 23), and every odd position bit is swapped with an adjacent on the left side.

# Example 1:
# Input: N = 23
# Output: 43
# Explanation: 
# Binary representation of the given number 
# is 00010111 after swapping 
# 00101011 = 43 in decimal.

# Example 2:
# Input: N = 2
# Output: 1
# Explanation: 
# Binary representation of the given number 
# is 10 after swapping 01 = 1 in decimal.

# Your Task: Your task is to complete the function swapBits() which takes an integer and returns an integer with all the odd and even bits swapped.


# Expected Time Complexity: O(1).
# Expected Auxiliary Space: O(1).

# Constraints:
# 1 ≤ N ≤ 10^9


class Solution:
    
    #Function to swap odd and even bits.
    def swapBits(self,n):
        even_mask = 0xAAAAAAAA
        odd_mask  = 0x55555555

        even = (n & even_mask) >> 1
        odd = (n & odd_mask) << 1

        return even | odd
# Time Complexity: O(1)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.swapBits(23))
    print(sol.swapBits(2))