def findPeak(arr, n):
    low, high = 0, n-1

    while low<=high:
        mid = (low+high) // 2
        
        if (mid == 0 or arr[mid-1]<=arr[mid]) and (mid==n-1 or arr[mid]>=arr[mid+1]):
            return mid
        
        elif mid>0 and arr[mid-1] > arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1


arr = [1, 3, 8, 12, 4, 2]
print(findPeak(arr, len(arr)))