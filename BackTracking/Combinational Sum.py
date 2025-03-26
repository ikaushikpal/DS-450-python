class Solution:
    def combinationalSum(self, arr, targetSum):
        self.finalResult = []
        self.depthAns = []

        arr = list(set(arr))
        arr.sort()
        self.combinationalSumUtil(arr, targetSum, 0, 0)

        for row in self.finalResult:
            print(row)

    def combinationalSumUtil(self, arr, targetSum, currentSum, index):
        if currentSum == targetSum:
            self.finalResult.append(self.depthAns.copy())
            return

        if len(arr) <= index or currentSum > targetSum:
            return
        
        for i in range(index, len(arr)):
            if currentSum+arr[i] > targetSum:
                return

            self.depthAns.append(arr[i])
            self.combinationalSumUtil(arr, targetSum, currentSum+arr[i], i)
            self.depthAns.pop()
        
    
        
if __name__ == '__main__':
    arr = [2, 4, 6, 8]
    targetSum = 8

    sol = Solution()
    sol.combinationalSum(arr, targetSum)
            

