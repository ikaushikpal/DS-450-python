from random import randint


def partition(arr, low, high):
    # just to randomize pivot element ---
    pivotIndex = randint(low, high)
    arr[low], arr[pivotIndex] = arr[pivotIndex], arr[low]
    # ----
    
    pivot = arr[low]
    i = low
    j = high

    while i < j:

        while i < high and arr[i] <= pivot:
            i += 1
             
        while j > low and arr[j] > pivot:
            j -= 1

        if(i < j):
            arr[i], arr[j] = arr[j], arr[i]
     
    arr[j], arr[low] = arr[low], arr[j]
    
    return j

def quickSort(arr, low, high):
    if low <= high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)


arr = [10, 16, 8, 12 , 15, 6, 3, 9, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print(arr)
