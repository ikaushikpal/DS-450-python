# not done
class Solution:
    def getMinDiff(self, arr, n, k):
        maxx = float('-inf')
        minn = float('inf')
        
        for i in range(n):
            h1 = max(arr[i] - k, 0)
            h2 = arr[i] + k
            
            maxx = max(h1, maxx)
            minn = min(h2, minn)
            
        return maxx - minn


if __name__ == '__main__':
    sol = Solution()
    sol.getMinDiff([2, 6, 3, 4, 7, 2, 10, 3, 2, 1], 10, 5)