# Given an array of integers (A[])  and a number x, find the smallest subarray with sum greater than the given value.

# Note: The answer always exists. It is guaranteed that x doesn't exceed the summation of a[i] (from 1 to N).

# Example 1:
# Input:
# A[] = {1, 4, 45, 6, 0, 19}
# x  =  51
# Output: 3
# Explanation:
# Minimum length subarray is 
# {4, 45, 6}

# Example 2:
# Input:
# A[] = {1, 10, 5, 2, 7}
#    x  = 9
# Output: 1
# Explanation:
# Minimum length subarray is {10}


class Solution:
    def sb(self, arr, n, x):
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
