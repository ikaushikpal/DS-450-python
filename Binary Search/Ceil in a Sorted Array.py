class Solution:
    def findCeil(self, arr, n, key):
        if key > arr[n-1]: return -1

        low, high = 0, n-1
        res = -1

        while low <= high:
            mid = (low+high)//2

            if arr[mid] == key:
                return mid
            
            elif arr[mid] < key:
                low = mid + 1       
            else:
                res = mid
                high = mid - 1

        return res