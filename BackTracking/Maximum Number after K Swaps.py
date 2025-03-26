class Solution:
    def findMaximumNum(self, string, k):
        self.max = int(string)
        self.findMaximumNumHelper(string, k, 0)
        return self.max
    
    def swap(self, string, i, j):
        return string[:i] + string[j] + string[i + 1:j] +string[i] + string[j + 1:]
    
    def findMaxIndices(self, string):
        maxDigit = int(string[0])
        indices = []

        for i, digit in enumerate(string):
            if int(digit) > maxDigit:
                maxDigit = int(digit)
                indices = [i]
            
            elif int(digit) == maxDigit:
                indices.append(i)
        
        return indices

    def findMaximumNumHelper(self, string, k, index):
        if k == 0 or index+1 == len(string):
            self.max = max(self.max, int(string))
            return
        
        currVal = string[index]
        maxIndices = self.findMaxIndices(string[index+1:])

        if currVal >= string[maxIndices[0] + index + 1]:
            self.findMaximumNumHelper(string, k, index + 1)
        
        else:
            for i in maxIndices:
                self.findMaximumNumHelper(self.swap(string, index, i + index + 1), k - 1, index+1)


    
if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaximumNum("12345", 2))
    print(sol.findMaximumNum("1199", 1))
    print(sol.findMaximumNum("129814999", 4))
    print(sol.findMaximumNum('1234567', 4))
