# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
 

# Example 1:

# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]

# Example 2:

# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]


from typing import List


class Solution:
    def findCeil(self, arr, n, key):
        if key > arr[n-1]: return n-1
        low, high = 0, n-1
        res = -1

        while low <= high:
            mid = (low+high)//2

            if arr[mid] == key:
                return mid
            
            elif arr[mid] < key:
                low = mid + 1       
            else:
                res = mid
                high = mid - 1

        return res
    
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        N = len(arr)
        ans = []
        
        pos = self.findCeil(arr, N, x)
        l = r = pos
        if arr[pos] == x:
            ans.append(x)
            r = (r + 1) % N  
        l = (l - 1 + N) % N
        
        while len(ans) < k:
            left_val, right_val = arr[l], arr[r]
            
            if abs(left_val - x) < abs(right_val - x):
                ans.append(left_val)
                l = (l - 1 + N) % N

            elif abs(left_val - x) > abs(right_val - x):
                ans.append(right_val)
                r = (r + 1) % N

            elif left_val < right_val:
                ans.append(left_val)
                l = (l - 1 + N) % N

            else:
                ans.append(right_val)
                r = (r + 1) % N
        
        ans.sort()
        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.findClosestElements([1,2,3,4,5], 4, 3))