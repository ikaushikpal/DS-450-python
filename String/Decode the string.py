# An encoded string (s) is given, the task is to decode it. The encoding pattern is that the occurance of the string is given at the starting of the string and each string is enclosed by square brackets.


# Example 1:
# Input: s = 1[b]
# Output: b
# Explanation: 'b' is present only one time.

# Example 2:
# Input: s = 3[b2[ca]]
# Output: bcacabcacabcaca
# Explanation: 2[ca] means 'ca' is repeated 
# twice which is 'caca' which concatenated with 
# 'b' becomes 'bcaca'. This string repeated 
# thrice becomes the output.


class Solution:
    def decodedString(self, s):
        def parse(token):
            n, c = 0, []
            
            while token and token[0] != ']':
                v = token.pop(0)

                if v.isnumeric():
                    n = n*10 + int(v)
                elif v != '[':
                    c.append(v)
                else:
                    nv = parse(token)
                    c.extend(nv*max(n, 1))
                    n = 0
                    
            if token:
                token.pop(0)
            return c
            
        return "".join(parse(list(s)))


if __name__ == '__main__':
    sol = Solution()
    print(sol.decodedString('3[a3[b]1[ab]]'))