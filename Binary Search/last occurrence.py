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