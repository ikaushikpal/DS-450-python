class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        return self.threeSum(arr)
        
    def twosum(self, arr, index, target):
        i = index
        j = len(arr) - 1

        while i<j:
            if arr[i] + arr[j] == target:
                return True
            
            elif arr[i] + arr[j] < target:
                i += 1
            else:
                j -= 1

    def threeSum(self, arr):
        self.res = 0
        arr.sort()

        for i in range(len(arr)-2):
            if (i==0) or (i and arr[i] != arr[i-1]):
                if self.twosum(arr, i+1, -arr[i]):
                    return 1
     
        return 0