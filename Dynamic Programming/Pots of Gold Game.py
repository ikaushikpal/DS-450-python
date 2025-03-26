# [same as] Optimal Strategy for a Game
class Solution:
    def helper(self, arr, i, j):
        if i > j:
            return 0
        
        if i == j:
            return arr[i]
            
        if (i, j) in self.memo:
            return self.memo[(i, j)]

        option1 = arr[i] + min(self.helper(arr,i+2,j), self.helper(arr,i+1,j-1))
        option2 = arr[j] + min(self.helper(arr,i,j-2), self.helper(arr,i+1,j-1))
        self.memo[(i, j)] = max(option1, option2)
        return self.memo[(i, j)]

    def maxCoins(self, arr, n):
        self.memo = {}
        return self.helper(arr, 0, n-1)
    
sol = Solution()
print(sol.maxCoins([8, 15, 3, 7], 4))