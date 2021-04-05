def count_subset_sum(arr, n,sum):
    if sum == 0: # if sum is zero means we found a subset whose sum is equal to sum(argument)
        return 1

    if n == 0: # if array is empty then there is no way make sum equals to zero
        return 0
    
    if sum >= arr[n - 1]:
        return count_subset_sum(arr, n-1, sum-arr[n-1]) + count_subset_sum(arr, n-1, sum)
    else:
        return count_subset_sum(arr, n-1, sum)


arr = [2, 3, 5, 6, 8, 10]
n = len(arr)
sum = 10
print(count_subset_sum(arr, n, sum))