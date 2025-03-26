# A step array is an array of integer where each element has a difference of at most k with its neighbor. Given a key x, we need to find the index value of x if multiple elements exist, return the first occurrence of the key.


# Example 1:
# â€‹Input : arr[ ] = {4, 5, 6, 7, 6}, K = 1 
#         and X = 6
# Output : 2
# Explanation:
# In an array arr 6 is present at index 2.
# So, return 2.


# â€‹Example 2:

# Input : arr[ ] = {20 40 50}, K = 20 
#         and X = 70
# Output :  -1 


def search (arr, N, x, k):
    i = 0
    while i < N:
        # if fount element x, return index
        if arr[i] == x:
            return i
        
        # lets say arr = [20, 40, 50, 70 ,70, 70, 60], k = 20, x = 60
        # i=0, so we can normally increment i by 1 or some value y
        # why y? because its given that the difference between adjacent elements is at most k
        # and we are going to use that to leverage the fact 
        # target is 60, current arr[i] = 20, so at best case each element is at most k away from target
        # ans 60-20 = 40, so diff is of 40, now k=20, so i can be incremented by 40/20 = 2
        # at best 60 is residing at index 2; here is given at most k
        # so array can also be [20, 21, 22, 23, ,,,,,,,, 60], k=20, x=60
        # in that case even if we increment i by 2, we will able to find 60
        i += max(1, (x - arr[i])//k)
    return -1