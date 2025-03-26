# Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
# Note: can you take care of the duplicates without using any additional Data Structure?

# Example 1:
# Input:
# n1 = 6; A = {1, 5, 10, 20, 40, 80}
# n2 = 5; B = {6, 7, 20, 80, 100}
# n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
# Output: 20 80
# Explanation: 20 and 80 are the only
# common elements in A, B and C.


class Solution:
    def findCommon(self, arr1, arr2):
        res= []
        i, j = 0, 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] == arr2[j]:
                res.append(arr1[i])

                while i<len(arr1) and arr1[i] == res[-1]: 
                    i += 1

                while j<len(arr2) and arr2[j] == res[-1]: 
                    j += 1

            elif arr1[i] < arr2[j]:
                i += 1
            else:
                j += 1
        
        return res

    def commonElements(self,A, B, C, n1, n2, n3):
        temp = self.findCommon(A, B)
        res = self.findCommon(temp, C)
        return res
# Time Complexity: O(n1 + n2 + n3) = O(N)
# Space Complexity: O(n1 + n2 + n3) = O(N)


if __name__ == '__main__':
    print(Solution().commonElements([1, 5, 10, 20, 40, 80], [6, 7, 20, 80, 100], [3, 4, 15, 20, 30, 70, 80, 120], 6, 5, 8))