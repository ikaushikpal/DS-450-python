class Solution:
	# @param A : tuple of integers
	# @return an integer
    def singleNumber(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        val = arr[0]
        for i in range(1, n):
            val ^= arr[i]

        return val
