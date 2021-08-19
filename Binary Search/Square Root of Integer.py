class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, num):
        low, high = 0, num
        floor_sqrt = 0

        while low <= high:
            mid = (low+high) // 2

            if mid*mid == num:
                return mid
            
            elif mid*mid < num:
                floor_sqrt = mid
                low = mid + 1
            
            else:
                high = mid - 1
        
        return floor_sqrt


print(Solution().sqrt(11))