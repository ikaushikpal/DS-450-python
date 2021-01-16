def insert(arr, value):
    if len(arr) == 0 or arr[-1] <= value:
        arr.append(value)
        return
    
    tempValue = arr.pop()
    insert(arr, value)
    insert(arr, tempValue)


def sort(arr):
    if len(arr) == 0:
        return
    tempVal = arr.pop()
    sort(arr)
    insert(arr, tempVal)



x = [1,3,2,5]
sort(x)
print(x)