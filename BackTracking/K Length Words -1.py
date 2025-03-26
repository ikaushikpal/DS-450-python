class Solution:
    def solution(self, string, k):
        self.util([0]*k, k, ''.join(set(string)))
    
    def util(self, box, k, remainingString):
        if k == 0:
            print(''.join(box))
            return
        
        if len(remainingString) == 0 or len(remainingString) < k: return

        self.util(box, k, remainingString[1:])
        for i in range(len(box)):
            if box[i] == 0:
                box[i] = remainingString[0]
                self.util(box, k-1, remainingString[1:])
                box[i] = 0



if __name__ == '__main__':
    sol = Solution()
    sol.solution('abcabc', 2)
    print('====')
    sol.solution('aabbbccdde', 3)