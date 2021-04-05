def binomialCoefficient(n, k):
	# since C(n, k) = C(n, n - k)
	if(k > n - k):
		k = n - k
	# initialize result
	res = 1
	# Calculate value of
	# [n * (n-1) *---* (n-k + 1)] / [k * (k-1) *----* 1]
	for i in range(k):
		res = res * (n - i)
		res = res / (i + 1)
	return res

# Driver program to test above function
n = 8
k = 2
res = binomialCoefficient(n, k)
print("Value of C(% d, % d) is % d" %(n, k, res))
