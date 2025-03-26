class Solution:
    def findFloor(self, arr, n, key):
        if key < arr[0]: return -1

        low, high = 0, n-1
        res = -1

        while low <= high:
            mid = (low+high)//2

            if arr[mid] == key:
                return mid
            
            elif arr[mid] < key:
                res = mid
                low = mid + 1
            
            else:
                high = mid - 1

        return res