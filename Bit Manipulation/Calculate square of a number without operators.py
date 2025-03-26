# Simple solution to calculate square without
# using * and pow()
def square(num):

	# Handle negative input
	if (num < 0):
		num = -num

	# Initialize result
	result, times = 0, num

	while times > 0:
		possibleShifts, currTimes = 0, 1

		while (currTimes << 1) <= times:
            
			currTimes = currTimes << 1
			possibleShifts += 1

		result = result + (num << possibleShifts)
		times = times - currTimes

	return result

# Driver Code

# Function calls
for n in range(10, 16):
	print("n =", n, ", n^2 =", square(n))

