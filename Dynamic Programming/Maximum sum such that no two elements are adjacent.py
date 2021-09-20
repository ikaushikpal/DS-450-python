class Recursive:
    def maxSumNoAdj(self, arr, prevIndex, currentIndex, n):
        if currentIndex == n:
            return 0
        
        if prevIndex + 1 == currentIndex:
            return self.maxSumNoAdj(arr, prevIndex, currentIndex+1, n)
        
        else:
            return max(arr[currentIndex]+self.maxSumNoAdj(arr, currentIndex, currentIndex+1, n), 
                        self.maxSumNoAdj(arr, prevIndex, currentIndex+1, n))


class MySolution:  
    def FindMaxSum(self, arr, n):
        if n == 0:
            return 0
        if n == 1:
            return arr[0]

        dpInclusive = [0] * n
        dpExclusive = [0] * n
        
        dpInclusive[0] = dpExclusive[1] = arr[0]
        dpInclusive[1] = arr[1]

        for i in range(2, n):
            dpInclusive[i] = arr[i] + max(dpInclusive[i-2], dpExclusive[i-2])
            dpExclusive[i] = max(dpInclusive[i-1], dpExclusive[i-1])

        return max(dpInclusive[n-1], dpExclusive[n-1])

class Solution:  
    def FindMaxSum(self, arr, n):
        if n == 0:
            return 0
        dpInclusive = [0] * n
        dpExclusive = [0] * n
        
        dpInclusive[0] = arr[0]

        for i in range(1, n):
            dpInclusive[i] = arr[i] + dpExclusive[i-1]
            dpExclusive[i] = max(dpInclusive[i-1], dpExclusive[i-1])

        return max(dpInclusive[n-1], dpExclusive[n-1])
    # space = O(n)

    def FindMaxSumConst(self, arr, n):
        if n == 0:
            return 0
        
        dpInclusive = arr[0]
        dpExclusive = 0

        for i in range(1, n):
            new_dpInclusive = arr[i] + dpExclusive
            new_dpExclusive = max(dpInclusive, dpExclusive)

            dpInclusive = new_dpInclusive
            dpExclusive = new_dpExclusive

        return max(dpInclusive, dpExclusive)
    # space = O(1)

if __name__ == '__main__':
    arr = [10, 5, 100, 70]
    print(Recursive().maxSumNoAdj(arr, -2, 0, len(arr)))

    arr = [5, 10, 10, 100, 5, 6]
    print(Recursive().maxSumNoAdj(arr, -2, 0, len(arr)))
    print(MySolution().FindMaxSum(arr, len(arr)))
    print(Solution().FindMaxSumConst(arr, len(arr)))