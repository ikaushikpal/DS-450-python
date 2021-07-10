# input:
# arr = [4, 6, 10], key = 7
# output: 6

# input:
# arr = [1, 3, 8, 10, 15], key = 12
# output: 10

# explanation:
#     [4, 6, 10]
#  abs 7  7   7
#      3, 1,  3 [1 is minimum diff so 6 is o/p]

# explanation:
#     [ 1, 3, 8, 10, 15]
#  abs 12  12 12 12   12
#      11, 9,  4 , 2,  3 [2 is minimum diff so 10 is o/p]


class MySolution:
    def findFloor(self, arr, n, key):
        if key < arr[0]: return 10**9

        low, high = 0, n-1
        res = 10**9

        while low <= high:
            mid = (low+high)//2

            if arr[mid] == key:
                return arr[mid]
            
            elif arr[mid] < key:
                res = arr[mid]
                low = mid + 1
            
            else:
                high = mid - 1

        return res
    
    def findCeil(self, arr, n, key):
        if key > arr[n-1]: return 10**9

        low, high = 0, n-1
        res = 10**9

        while low <= high:
            mid = (low+high)//2

            if arr[mid] == key:
                return mid
            
            elif arr[mid] < key:
                low = mid + 1       
            else:
                res = arr[mid]
                high = mid - 1

        return res
    
    def minimumDiff(self, arr, n, key):
        floor = self.findFloor(arr, n, key)
        floor_abs = abs(floor - key)

        if floor_abs <= 1:
            return floor
        
        ceil = self.findCeil(arr, n, key)
        ceil_abs = abs(ceil - key)

        if floor_abs < ceil_abs:
            return floor
        else:
            return ceil
    

class AdiSolution:
    def minimumDiff(self, arr, n, key):
        floor = ceil = 10**9
        low, high = 0, n-1

        while low <= high:
            mid = (low+high) // 2

            if arr[mid] == key:
                return arr[mid]
            
            elif arr[mid] > key:
                ceil = arr[mid]
                high = mid - 1
            else:
                floor = arr[mid]
                low = mid + 1
        
        floor_abs = abs(floor - key)
        ceil_abs = abs(ceil - key)

        if floor_abs < ceil_abs:
            return floor
        else:
            return ceil
