# Given an infinite sorted array consisting 0s and 1s. The problem is to find the index of first ‘1’ in that array. As the array is infinite, therefore it is guaranteed that number ‘1’ will be present in the array.
# Examples: 
 

# Input : arr[] = {0, 0, 1, 1, 1, 1} 
# Output : 2

# Input : arr[] = {1, 1, 1, 1,, 1, 1}
# Output : 0


def findFirstOccurrence(arr, low, high, key):
    res = -1

    while low<=high:
        mid = (low+high) // 2

        if arr[mid] == key:
            res = mid
            high = mid - 1
        
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
        
    return res


def findLocINF(arr):
    key = 1
    low, high = 0, 1

    while arr[high] < key:
        low = high
        high *= 2
    
    return findFirstOccurrence(arr, low, high, key)



if __name__ == '__main__':
    arr = [0, 0, 1, 1, 1, 1]

    print(findLocINF(arr))
