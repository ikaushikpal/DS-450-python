def circularTour(arr):
    gas_balance = 0

    startIndex = 0
    prevCost = 0

    for i in range(len(arr)):
        gas_balance += arr[i][0] - arr[i][1]

        if gas_balance < 0:
            startIndex = i+1
            prevCost += gas_balance
            gas_balance = 0
    
    if gas_balance + prevCost >= 0:
        return startIndex
    else:
        return -1


arr = [[4, 6], [6,5], [7, 3], [4,5]]
print(circularTour(arr))