# Given a string S, return the sum of beauty of all its substrings.
# The beauty of a string is defined as the difference in frequencies between the most frequent and least frequent characters.

# For example, the beauty of string "aaac" is 3 - 1 = 2.
# Example 1:

# Input:
# S = "aaac"
# Output:
# 3
# Explanation: The substrings with non - zero beauty are ["aaac","aac"] where beauty of "aaac" is 2 and beauty of "aac" is 1.
 

# Example 2:

# Input:
# S = "geeksforgeeks"
# Output:
# 62


class Solution:
    def beautySum(self, s):
        beauty=0

        for i in range (len(s)):
            ch = {}
            for j in range (i,len(s)):
                ch[s[j]] = ch.get(s[j], 0) + 1
                beauty += max(ch.values()) - min(ch.values())
        return beauty
# Time Complexity: O(|S|^2)
# Auxiliary Space: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.beautySum('aaac'))
    print(sol.beautySum('geeksforgeeks'))