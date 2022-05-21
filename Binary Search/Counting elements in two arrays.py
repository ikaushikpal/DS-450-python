# Given two unsorted arrays arr1[] and arr2[]. They may contain duplicates. For each element in arr1[] count elements less than or equal to it in array arr2[].

# Example 1:
# Input:
# m = 6, n = 6
# arr1[] = {1,2,3,4,7,9}
# arr2[] = {0,1,2,1,1,4}
# Output: 4 5 5 6 6 6
# Explanation: Number of elements less than
# or equal to 1, 2, 3, 4, 7, and 9 in the
# second array are respectively 4,5,5,6,6,6

# Example 2:
# Input:
# m = 5, n = 7
# arr1[] = {4 8 7 5 1}
# arr2[] = {4,48,3,0,1,1,5}
# Output: 5 6 6 6 3

# Your Task :
# Complete the function countEleLessThanOrEqual() that takes two array arr1[], arr2[],  m, and n as input and returns an array containing the required results(the count of elements less than or equal to it in arr2 for each element in arr1 where ith output represents the count for ith element in arr1.)

class Solution:
    def ceil(self, arr, key):
        low, high = 0, len(arr)-1

        while low <= high:
            mid = (low + high) >> 1

            if arr[mid] <= key:
                low = mid + 1
            else:
                high = mid - 1
        
        return low

    def countEleLessThanOrEqual(self,arr1,n1,arr2,n2):
        ans = []
        arr2.sort()

        for key in arr1:
            if key < arr2[0]:
                ans.append(0)
            elif key > arr2[-1]:
                ans.append(n2)
            else:
                ans.append(self.ceil(arr2, key))
        
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.countEleLessThanOrEqual([1,2,3,4,7,9], 6,
                                      [0,1,2,1,1,4], 6))
        
