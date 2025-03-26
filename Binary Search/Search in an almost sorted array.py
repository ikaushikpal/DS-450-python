def modifiedBS(arr, n, key):
    low, high = 0, n-1

    while low <= high:
        mid = (low+high) // 2

        if arr[mid] == key: return mid
        if mid-1>=0 and arr[mid-1] == key: return mid-1
        if mid+1<n and arr[mid+1] == key: return mid+1

        elif arr[mid] < key:
            low = mid + 2
        else:
            high = mid - 2

    return -1

    