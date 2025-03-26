# class Solution:
#     def helper(self, s, t, w):
#         if len(s) == 0 and len(t) == 0:
#             self.ans = min(self.ans, w)
#             return
        
#         if len(t) > 0:
#             self.helper(s, t[:-1], w + t[-1])
            
#         if len(s) > 0:
#             self.helper(s[1: ], t + s[0], w)

#     def robotWithString(self, s: str) -> str:
#         self.ans = 'z' * len(s)
#         self.helper(s, '', '')
#         return self.ans



class Solution:
    def helper(self, s, t, w, size):
        if len(s) == 0 and len(t) == 0:
            self.ans = min(self.ans, w)
            return
        
        # if (s, t) in self.memo:
        #     return self.memo[(s, t)]
        
        ans = 'z' * size
        if len(t) > 0:
            self.helper(s, t[:-1], w + t[-1], size)
            
        if len(s) > 0:
            self.helper(s[1: ], t + s[0], w, size)
        
        # self.memo[(s, t)] = ans
        # return ans

    def robotWithString(self, s: str) -> str:
        self.memo = {}
        self.ans = 'z' * len(s)
        self.helper(s, '', '', len(s))
        return self.ans
print(Solution().robotWithString('zza'))