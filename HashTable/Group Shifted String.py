# Given an array of strings (all lowercase letters), the task is to group them in such a way that all strings in a group are shifted versions of each other. Two string S and T are called shifted if, 

# S.length = T.length 
# and
# S[i] = T[i] + K for 
# 1 <= i <= S.length  for a constant integer K
# For example strings, {acd, dfg, wyz, yab, mop} are shifted versions of each other.

# Input  : str[] = {"acd", "dfg", "wyz", "yab", "mop",
#                  "bdfh", "a", "x", "moqs"};

# Output : a x
#          acd dfg wyz yab mop
#          bdfh moqs
# All shifted strings are grouped together.


from collections import defaultdict
from typing import List


class Solution:
    def serialize(self, s: str) -> str:
        msg = ''
        for i in range(1, len(s)):
            prevChar = ord(s[i - 1])
            currChar = ord(s[i])
            diff = prevChar - currChar
            if diff < 0:
                diff = (diff + 26) % 26
            msg = f'{msg}-{diff}'
        return msg

    def groupShifted(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            text = self.serialize(s)
            groups[text].append(s)
        
        return list(groups.values())
# Time Complexity: O(N)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.groupShifted(["acd", "dfg", "wyz", "yab", "mop", "bdfh", "a", "x", "moqs"]))