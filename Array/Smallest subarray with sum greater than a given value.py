def solve(arr, x):
    n = len(arr)

    if n <= 1:
        return n

    startWindow = 0
    endWindow = 0
    minLength = 10**9
    currentSum = 0

    while True:        
        while startWindow < n and currentSum > x:
            windowSize = endWindow - startWindow
            minLength = min(minLength, windowSize)

            currentSum -= arr[startWindow]
            startWindow += 1


        while endWindow<n and currentSum <= x:
            currentSum += arr[endWindow]
            endWindow += 1
        
        if endWindow >= n and currentSum<=x:
            break


    if minLength == 10**9:
        return -1
    else:
        return minLength


arr = [1, 4, 45, 6, 0, 19]
targetSum = 51
print(solve(arr, targetSum))

print(solve([1, 10, 5, 2, 7], 9))
print(solve([1, 11, 100, 1, 0, 200, 3, 2, 1, 250], 280))
print(solve([1, 2, 4], 8))
