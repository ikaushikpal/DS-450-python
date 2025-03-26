# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true


# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false


from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            
            prevFlower = 0 if i == 0 else flowerbed[i - 1]
            nextFlower = 0 if i == len(flowerbed) - 1 else flowerbed[i + 1]
            if prevFlower == nextFlower == 0:
                flowerbed[i] = 1
                n -= 1
        
            if n == 0:
                return True
        return False
# Time Complexity: O(n)
# Space Complexity: O(1)


if __name__ == '__main__':
    flowerbed = [1,0,0,0,1]
    n = 1
    print(Solution().canPlaceFlowers(flowerbed, n))

    flowerbed = [1,0,0,0,1]
    n = 2
    print(Solution().canPlaceFlowers(flowerbed, n))