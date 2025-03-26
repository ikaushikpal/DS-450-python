from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        maxWater = 0

        while i < j:
            width = j - i
            height = min(heights[i], heights[j])
            water = width * height

            maxWater = max(maxWater, water)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return maxWater