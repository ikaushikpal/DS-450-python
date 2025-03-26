# https://www.interviewbit.com/problems/woodcutting-made-easy/

# Problem states that we need to find minimum height where we cut all above height
# trees then sum of cutted wood be same of req wood of ceil of that
# We need to return minimum height where we cut all trees above that height se got our
# required wood
# 
# this problem approach is very same with book allocation problem
# here we also use a line to represent minimumHeight


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def getWood(self, treesHeight, height):
        totalWood = 0

        for treeHeight in treesHeight:
            if treeHeight > height:
                totalWood += (treeHeight - height)

        return totalWood

    def solve(self, treesHeight, requiredWood):
        lowestHeight, highestHeight = 0, max(treesHeight) 
        # lowestHeight in a sense that above that height we will get maximum wood
        # highestHeight in a sense that above that height we will get minimum wood

        # from 0 height will get sum(treesHeight) wood
        # from max(treesHeight) will get 0 wood

        minimumHeightNeeded = 0 # 0 is maximum value in a sense that all trees will be cut from bottom
        # and we will get highestHeightest amount of woods

        while lowestHeight<=highestHeight:

            mid = (lowestHeight+highestHeight)//2

            gotWood = self.getWood(treesHeight, mid)
            # gotWood denotes how much wood we will get from cutting that height

            if gotWood == requiredWood:
                return mid # if we find exactly same amount of wood for requirement
            
            elif gotWood > requiredWood:
                minimumHeightNeeded = mid # storing for ceil
                lowestHeight = mid +1

            else:
                highestHeight = mid - 1
        
        return minimumHeightNeeded