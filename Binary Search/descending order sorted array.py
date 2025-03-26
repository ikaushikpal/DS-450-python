def reversedBinarySearch(arr, n, key):
        low, high = 0, n-1
        
        while low <= high:
            mid = (low+high)//2

            if arr[mid] == key:
                return mid
            
            elif arr[mid] > key:
                low = mid + 1
            
            else:
                high = mid - 1

        return -1