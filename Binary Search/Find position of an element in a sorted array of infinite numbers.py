# Suppose you have a sorted array of infinite numbers, how would you search an element in the array?
# Source: Amazon Interview Experience. 
# Since array is sorted, the first thing clicks into mind is binary search, but the problem here is that we don’t know size of array. 
# If the array is infinite, that means we don’t have proper bounds to apply binary search. So in order to find position of key, first we find bounds and then apply binary search algorithm.
# Let low be pointing to 1st element and high pointing to 2nd element of array, Now compare key with high index element, 
# ->if it is greater than high index element then copy high index in low index and double the high index. 
# ->if it is smaller, then apply binary search on high and low indices found. 


def binarySearch(arr, low, high, key):
    while low<=high:
        mid = (low+high) // 2

        if arr[mid] == key:
            return mid
        
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
        
    return -1


def findLocINF(arr, key):
    low, high = 0, 1

    while arr[high] < key:
        low = high
        high *= 2
    
    return binarySearch(arr, low, high, key)



if __name__ == '__main__':
    arr = [_ for _ in range(1, 50)]
    key = 7

    print(findLocINF(arr, key))
