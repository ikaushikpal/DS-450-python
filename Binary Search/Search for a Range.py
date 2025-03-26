class Solution:

    def firstOccurrence(self, array:list, key:int, low:int, high:int)->int:
        first = -1

        while low<=high:
            mid = (low+high) // 2

            if array[mid] == key:
                first = mid
                high = mid-1
                
            elif array[mid] < key:
                low = mid + 1
            
            else:
                high = mid - 1
        
        return first

    def lastOccurrence(self, array:list, key:int, low:int, high:int)->int:
        last = -1

        while low<=high:
            mid = (low+high) // 2

            if array[mid] == key:
                last = mid
                low = mid+1
                
            elif array[mid] < key:
                low = mid + 1
            
            else:
                high = mid - 1
        
        return last
    
    def searchRange(self, array:list, key:int)->list:
        n = len(array)

        firstOcc = self.firstOccurrence(array, key, 0, n-1)
        if firstOcc == -1:
            return [-1, -1]
        
        lastOcc = self.lastOccurrence(array, key, firstOcc, n-1)

        return [firstOcc, lastOcc]



if __name__ == '__main__':
    arr = [5, 7, 7, 8, 8, 10]
    key = 8
    sol = Solution()
    print(sol.searchRange(arr, key))