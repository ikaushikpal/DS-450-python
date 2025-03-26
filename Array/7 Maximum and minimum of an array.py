def getMinMax(arr: list, n: int) -> pair:
    max = min = 0
    if n == 1:
        max = arr[0]
        min = arr[0]
        return minmax

    if arr[0] > arr[1]:
        max = arr[0]
        min = arr[1]
    else:
        max = arr[1]
        min = arr[0]

    for i in range(2, n):
        if arr[i] > max:
            max = arr[i]
        elif arr[i] < min:
            min = arr[i]

    return min, max
