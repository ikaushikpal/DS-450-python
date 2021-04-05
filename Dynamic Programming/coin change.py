def coin_change(arr, m, n):
	if m == 0 : 
		return 1
	if n == 0 :
		return 0

	if m >= arr[n-1]:
		return coin_change(arr, m-arr[n-1], n) + coin_change(arr, m, n-1) 
	else:
		return coin_change(arr, m, n-1) 




arr =[2, 5, 3, 6]
m = 10
n = 4


print(coin_change(arr, m, n)) 