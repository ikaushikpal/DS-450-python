class Solution:
    def findKRotation(self,arr,n):
        if arr[0] < arr[n-1]:
            return 0

        pivot = -1
        low, high= 0, n-1

        while low <= high:
            if arr[low] < arr[high]:
                return low

            mid = low + (high-low)//2
            
            mid_next = (mid+1)%n
            mid_prev = (mid-1+n)%n

            if arr[mid] <= arr[mid_next] and arr[mid] <= arr[mid_prev]:
                pivot = mid;
                break
                
            elif arr[low] <= arr[mid]:
                low = mid + 1;

            elif arr[mid] <= arr[high]:
                high = mid - 1;
        
        return pivot