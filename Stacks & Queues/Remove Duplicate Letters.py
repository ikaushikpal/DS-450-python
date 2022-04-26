# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

# Example 1:

# Input: s = "bcabc"
# Output: "abc"

# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"


from collections import Counter, deque


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = deque()
        freq = Counter(s)
        used = {}
        
        for char in s:
            # every time decrement the frequency of the char
            freq[char] -= 1
            
            # check if this char is already used then it means
            # char is used such that in middle of some sequence
            # ex: stack = [a, c, d] now char is c
            # c is already used and we cannot remove d because d only occurred once
            # so just don't add it to stack
            if char in used and used[char]:
                continue
            
            # performing monotonic stack
            # poping every time if char is lexicographically smaller than the top of stack
            # also need to check if we can even remove top of stack
            # because it may happen that top of stack is z and it only occurred once and char is a
            while stack and stack[-1] >= char and freq[stack[-1]] > 0:
                # those elements poping from stack
                # need to make sure that they can occur again
                used[stack.pop()] = False
            
            # adding char to stack
            # and also making used[char] = True
            # so we know that we used char previously
            stack.append(char)
            used[char] = True
        
        return ''.join(stack)


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicateLetters('bcabc'))
    print(sol.removeDuplicateLetters('cbacdcbc'))