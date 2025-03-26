# You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

# We repeatedly make k duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

 

# Example 1:
# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete.


# Example 2:
# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation: 
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"


# Example 3:
# Input: s = "pbbcggttciiippooaais", k = 2
# Output: "ps"


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # (character, count)
        for char in s:
            if len(stack) > 0:
                # if char is same as top of stack
                if stack[-1][0] == char:
                    _, f = stack.pop()
                    # increment frequency
                    newF = f + 1

                    # if now frequency is >= k then reduce by k
                    # why? because we need to delete adjacent chars 
                    if newF >= k:
                        newF -= k
                    
                    if newF > 0:
                        stack.append((char, newF))     
                else:
                    stack.append((char, 1))
            else:
                stack.append((char, 1))
        
        newS = ''
        while stack:
            char, freq = stack.pop()
            newS = f'{newS}{char * freq}'
        
        return newS[::-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicates(s = "deeedbbcccbdaa", k = 3))
