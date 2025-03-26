# Problem Description

# Given a sorted array A and a target value B, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array. (Imp)

# **Example Input**
# Input 1:

#  A = [1, 3, 5, 6]
# B = 5
# Input 2:

#  A = [1, 3, 5, 6]
# B = 2


# **Example Output**
# Output 1:

#  2
# Output 2:

#  1

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, array, key):
        low, high = 0, len(array)-1

        index = len(array)
        # if key is larger than max of arr then
        # insertion position should be nth index

        while low <= high:
            mid = (low + high) // 2
            
            if array[mid] == key:
                return mid
            
            elif array[mid] > key:
                index = mid
                high = mid - 1
            
            else:
                low = mid + 1
        
        return index
