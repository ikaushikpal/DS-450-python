class Solution:
    def solution(self, string, k):
        uniqueChar = {}
        for s in string:
            if s not in uniqueChar:
                uniqueChar[s] = False
        
        self.util('', k, ''.join(uniqueChar))

    def util(self, output, k, uniqueCharSeq):
        if k == 0:
            print(output)
            return
        
        for i in range(len(uniqueCharSeq)):
            self.util(output+uniqueCharSeq[i], k-1, uniqueCharSeq[i+1:])
    


if __name__ == '__main__':
    sol = Solution()
    sol.solution('aabbbccdde', 3)