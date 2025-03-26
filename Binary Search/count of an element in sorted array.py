def firstOccurrence(arr, n, key):
    low, high = 0, n-1
    res = -1

    while low <= high:
        mid = (low+high)//2

        if arr[mid] == key:
            res = mid
            high = mid -1
        
        elif arr[mid] < key:
            low = mid + 1
        
        else:
            high = mid - 1

    return res

def lastOccurrence(arr, n, key):
    low, high = 0, n-1
    res = -1

    while low <= high:
        mid = (low+high)//2

        if arr[mid] == key:
            res = mid
            low = mid +1
        
        elif arr[mid] < key:
            low = mid + 1
        
        else:
            high = mid - 1

    return res

def count(arr, n, key):
    last = lastOccurrence(arr, n, key)
    first = firstOccurrence(arr, n, key)
    
    if last == -1:
        return 0
    else:
        return last - first + 1
