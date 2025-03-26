def maxSumK(arr, n, k):
    i= j = 0
    max_sum =  -10e6
    sum = 0

    for j in range(0, n):
        if j-i + 1 < k:
            sum += arr[j]
        
        if j-i + 1 == k:
            sum += arr[j]
            max_sum = max(max_sum, sum)
            sum -= arr[i]
            i += 1
            
    return max_sum


def maxSumK2(arr, n, k):
    max_sum = - 10e6
    sum = 0

    for i in range(k-1):
        sum += arr[i]
    
    for i in range(k-1, n):
        sum += arr[i]
        max_sum = max(max_sum, sum)
        sum -= arr[i-k+1]
    
    return max_sum

arr = [2, 5, 1, 8, 10, 10, 10]
n = len(arr)
k = 3

print(maxSumK(arr, n, k))
print(maxSumK2(arr, n, k))