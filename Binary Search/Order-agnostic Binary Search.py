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

def binarySearch(arr, n, key):
        low, high = 0, n-1
        
        while low <= high:
            mid = (low+high)//2

            if arr[mid] == key:
                return mid
            
            elif arr[mid] < key:
                low = mid + 1
            
            else:
                high = mid - 1

        return -1

def orderAgonsticBS(arr, n, key):
    if len(arr) == 0 : return -1

    if len(arr) == 1:
        if arr[0] == key: return 0
        else: return -1
    
    if arr[0] < arr[1]:
        return binarySearch(arr, n, key)
    else:
        return reversedBinarySearch(arr, n, key)