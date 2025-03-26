# Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.

# Every house can be warmed, as long as the house is within the heater's warm radius range. 

# Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so that those heaters could cover all houses.

# Notice that all the heaters follow your radius standard, and the warm radius will the same.

# Example 1:
# Input: houses = [1,2,3], heaters = [2]
# Output: 1
# Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.

# Example 2:
# Input: houses = [1,2,3,4], heaters = [1,4]
# Output: 1
# Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.

# Example 3:
# Input: houses = [1,5], heaters = [2]
# Output: 3


from turtle import left
from typing import List


class Solution:
    def findFloor(self, arr, key):
        low, high = 0, len(arr)-1
        res = -1

        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == key:
                return key
            elif arr[mid] < key:
                res = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return arr[res]
    
    def findCeil(self, arr, key):
        low, high = 0, len(arr)-1
        res = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == key:
                return key
            elif arr[mid] < key:
                low = mid + 1
            else:
                res = mid
                high = mid - 1
                
        return arr[res]

    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        minRadius = 0
        heaters.sort()

        for house in houses:
            leftHeaterDist = abs(house - self.findFloor(heaters, house))
            rightHeaterDist = abs(self.findCeil(heaters, house) - house)
            minRadius = max(minRadius, min(leftHeaterDist, rightHeaterDist))

        return minRadius


if __name__ == '__main__':
    sol = Solution()
    print(sol.findRadius([1,2,3], [2]))
    print(sol.findRadius(houses = [1,2,3,4], heaters = [1,4]))
    print(sol.findRadius(houses = [1,5], heaters = [2]))
    print(sol.findRadius([1,5], [10]))