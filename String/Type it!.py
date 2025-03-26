# Geek is extremely punctual but today even he is not feeling like doing his homework assignment. He must start doing it immediately in order to meet the deadline. For the assignment, Geek needs to type a string s.
# To reduce his workload, he has decided to perform one of the following two operations till he gets the string.

# Append a character at the end of the string.
# Append the string formed thus far to the end of the string. (This can not be done more than once.)
# Help Geek find the minimum operations required to type the given string.


# Example 1:
# Input:
# s = abcabca
# Output: 5
# Explanation: a -> ab -> abc -> abcabc 
# -> abcabca


# Example 2:
# Input:
# s = abcdefgh
# Output: 8
# Explanation: a -> ab -> abc -> abcd 
# -> abcde -> abcdef -> abcdefg -> abcdefgh


class Solution:
    def minOperation(self, s): 
        N = len(s)
        for i in range(N//2-1, -1, -1):
            if s[:i+1] == s[i+1:2*(i+1)]:
                return N - i
        return N 
# Time complexity: O(N^2)
# Space complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minOperation('abcabca'))
    print(sol.minOperation('abcdefgh'))