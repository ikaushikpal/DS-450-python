# Given a string S consisting of only lowercase characters. Find the lexicographically smallest string after removing exactly k characters from the string. But you have to correct the value of k, i.e., if the length of the string is a power of 2, reduce k by half, else multiply k by 2. You can remove any k character.
# NOTE: If it is not possible to remove k (the value of k after correction) characters or if the resulting string is empty return -1.

# Example 1:
# Input: S = "fooland", k = 2
# Output: "and" 
# Explanation: As the size of the string = 7
# which is not a power of 2, hence k = 4.
# After removing 4 characters from the given 
# string, the lexicographically smallest
# string is "and".


# Example 2:
# Input: S = "code", k = 4
# Output: "cd"
# Explanation: As the length of the string = 4, 
# which is 2 to the power 2, hence k = 2.
# Hence, lexicographically smallest string after 
# removal of 2 characters is "cd".


from collections import deque


class Solution:
    def isPowerOfTwo(self, num):
        return num & (num - 1) == 0
        
    def lexicographicallySmallest(self, string, k):
        if self.isPowerOfTwo(len(string)):
            k = k >> 1
        else:
            k = k << 1
        
        if k >= len(string):
            return -1
            
        stack = deque()
        for i, char in enumerate(string):
            while stack and k > 0 and stack[-1] > char:
                stack.pop()
                k -= 1
                
            if k == 0:
                return ''.join(stack) + string[i : ]
            stack.append(char)
        
        for _ in range(len(stack) - k - 1):
            stack.pop()
            
        return ''.join(stack)
# T.C. = O(N + K)
# S.C. = O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.lexicographicallySmallest("fooland", 2))
    print(sol.lexicographicallySmallest("code", 4))