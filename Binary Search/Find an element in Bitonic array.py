# Given a bitonic sequence of n distinct elements, write a program to find a given element x in the bitonic sequence in O(log n) time. A Bitonic Sequence is a sequence of numbers that is first strictly increasing then after a point strictly decreasing.

# Examples: 

# Input :  arr[] = {-3, 9, 18, 20, 17, 5, 1};
#          key = 20
# Output : Found at index 3

# Input :  arr[] = {5, 6, 7, 8, 9, 10, 3, 2, 1};
#          key = 30
# Output : Not Found


def findPeak(arr, n):
    low, high = 0, n-1
    while low<=high:
        mid = (low + high) // 2

        if (mid==0 or arr[mid-1]<=arr[mid]) and (mid==n-1 or arr[mid]>=arr[mid+1]):
            return mid
        
        elif mid>0 and arr[mid-1] > arr[mid]:
            high = mid-1
        else:
            low = mid + 1
    
    return -1

def binarySearch(arr, low, high, key, ascending=True):
    while low<=high:
        mid = (low+high) // 2

        if arr[mid] == key: return mid

        elif (ascending and arr[mid] > key) or (not ascending and arr[mid] < key):
            high = mid - 1

        elif (ascending and arr[mid] < key) or (not ascending and arr[mid] > key):
            low = mid + 1
    
    return -1

def findElementBitonic(arr, n, key):
    peak = findPeak(arr, n)

    if key > arr[peak]:
        return -1

    if arr[peak] == key:
        return peak
    
    left = binarySearch(arr, 0, peak, key, ascending=True)
    if left!=-1: return left

    right = binarySearch(arr, peak+1, n-1, key, ascending=False)
    return right


if __name__ == '__main__':
    arr = [-3, 9, 18, 20, 17, 5, 1]
    key = 20
    
    print(findElementBitonic(arr, len(arr), key))

    arr = [5, 6, 7, 8, 9, 10, 3, 2, 1]
    key = 30
    
    print(findElementBitonic(arr, len(arr), key))
