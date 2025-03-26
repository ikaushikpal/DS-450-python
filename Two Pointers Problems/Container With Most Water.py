class Solution:
	# @param A : list of integers
	# @return an integer
    def maxArea(self, A):
        i = 0
        n = len(A)
        j = n-1
        maxArea = n-1 * min(A[0], A[n-1])

        while i<n and j>=0 and i<j:
            area = (j-i) * min(A[i], A[j])
            
            if area > maxArea:
                maxArea = area
                
            if A[i] > A[j]:
                j -= 1
            else:
                i += 1

        return maxArea 