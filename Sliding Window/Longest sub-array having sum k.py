
# for positive values only
def variableSizeWindow(arr, n, k):
    current_sum = i = j = 0
    max_window = -10e6

    while j < n:
        if current_sum < k:
            current_sum += arr[j]
            j += 1

        if current_sum > k:
            current_sum -= arr[i]
            i += 1

        if current_sum == k:
            max_window = max(max_window, j-i)
            current_sum -= arr[i]
            i += 1
    
    return max_window

def variableSizeWindow2(arr, n, k):
    mydict = dict()
  
    # Initialize sum and maxLen with 0
    sum = 0
    maxLen = 0
  
    # traverse the given array
    for i in range(n):
  
        # accumulate the sum
        sum += arr[i]
  
        # when subArray starts from index '0'
        if (sum == k):
            maxLen = i + 1
  
        # check if 'sum-k' is present in
        # mydict or not
        elif (sum - k) in mydict:
            maxLen = max(maxLen, i - mydict[sum - k])
  
        # if sum is not present in dictionary
        # push it in the dictionary with its index
        if sum not in mydict:
            mydict[sum] = i
        
    return maxLen

if __name__ == '__main__':
    k=5
    arr=[4, 1, 1, 1, 2, 3, 5]
    n = len(arr)

    res = variableSizeWindow(arr, n, k)
    print(res)

    res = variableSizeWindow([10, 5, 2, 7, 1, 9], 6, 15)
    print(res)

    res = variableSizeWindow2([-5, 8, -14, 2, 4, 12], 6, -5)
    print(res)

    res = variableSizeWindow2([10, 5, 2, 7, 1, 9], 6, 15)
    print(res)