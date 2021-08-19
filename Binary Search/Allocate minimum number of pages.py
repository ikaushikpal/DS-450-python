# https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1


class Solution:
    def findMaxSum(self, arr, n):
        maxEle = arr[0]
        total = arr[0]
        for i in range(1, n):
            if arr[i] > maxEle:
                maxEle = arr[i]
            
            total += arr[i]
        
        return (maxEle, total)

    def isValid(self, arr, n ,k, maxPages):
        students = 1
        currentSum = 0
        
        for val in arr:
            if val > maxPages:
                return False

            currentSum += val

            if currentSum > maxPages:
                students += 1
                currentSum = val
            
                if students > k:
                    return False

        return True

    #Function to find minimum number of pages.
    def findPages(self, arr, n, k):
        if k>n:
            return -1
        
        if n==0 and k==0:
            return 0
        
        maxEle, total = self.findMaxSum(arr, n)

        if k <= 1:
            return total
        
        if k==n:
            return maxEle
        
        low, high = maxEle, total
        res = -1

        while low<=high:
            mid = (low+high) // 2

            if self.isValid(arr, n ,k, mid):               
                res = mid
                high = mid - 1

            else:
                low = mid + 1
        
        return res


print(Solution().findPages([10, 20, 30, 40], 4, 2))

