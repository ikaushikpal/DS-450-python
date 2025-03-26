# # HARD
# A car travels from a starting position to a destination which is target miles east of the starting position.

# There are gas stations along the way. The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.

# The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

# Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.

# Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

 
# Example 1:
# Input: target = 1, startFuel = 1, stations = []
# Output: 0
# Explanation: We can reach the target without refueling.


# Example 2:
# Input: target = 100, startFuel = 1, stations = [[10,100]]
# Output: -1
# Explanation: We can not reach the target (or even the first gas station).


# Example 3:
# Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
# Output: 2
# Explanation: We start with 10 liters of fuel.
# We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
# Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
# and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
# We made 2 refueling stops along the way, so we return 2.

# NOTE:
# Let's start with an example:

# Start at 0, with start fuel = 35
# Stations = [(10, 25), (20, 12), (30,21), (40, 5), (50,3)]
# 35.......25.......12.......21.......5........3................... (fuel)
# |--------|--------|--------|--------|--------|------------------> (stations)
# 0.......10.......20.......30........40.......50.................. (distance)

# Obviously, with 0 steps, the max distance we can reach is 35.
# The question now is with 1 steps, what is the max distance we can reach?

# 35.......25.......12.......21.......5........3................... (fuel)
# |--------|--------|--------|--------|--------|------------------> (stations)
# 0.......10.......20.......30...|....40.......50.................. (distance)
# ...............................|.................................
# ...............................35................................ (max distance can reach after 0 step)

# When we reach 35, we pass by 3 stations [10, 20, 30]. It means we can possibly refuel at these stations.

# Refuel at 10: max distance = 10 + (35 - 10 + 25) = 35 + 25 = 60
# Refuel at 20: max distance = 20 + (35 - 20 + 12) = 35 + 12 = 47
# Refuel at 30: max distance = 30 + (35 - 30 + 21) = 35 + 21 = 56
# We notice that apparently the max distance does not depends on the station's position, but the station's fuel.
# Apparently, the maximum distance of k+1 steps = maximum distance of k steps + maximum fuel of stations that the car has passed by (counting from the last station that makes the previous maximum distance)

# 35......[25]......12.......21.......5........3................... (fuel)
# |--------|--------|--------|--------|--------|------------------> (stations)
# 0.......[10]......20.......30...|...40.......50.................. (distance)
# ...............................|....................|............
# ...............................35...................|............ (max distance can reach after 0 step)
# ....................................................60........... (max distance can reach after 1 step)

# When we reach 60, we reach more 2 stations [40, 50], so if :

# Refuel at 20: max distance = 10 + (60-10) - (20-10) + (20-10) + 12 = 60 + 12 = 72
# Refuel at 30: max distance = 10 + (60-10) - (30-10) + (30-10) + 21 = 60 + 21 = 81
# Refuel at 40: max distance = 10 + (60-10) - (40-10) + (40-10) + 5 = 60 + 5 = 65
# Refuel at 50: max distance = 10 + (60-10) - (50-10) + (50-10) + 3 = 60 + 3 = 63
# Our guess is correct, the max distance only depends on the amount of fuel at each station. And each time, we should choose the largest amount of fuel
import heapq
from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # Approach
        # go until we exhaust our fuel supply 
        # then take maximum fuel 
        maxHeap = []
        canGo = startFuel
        refillCount = 0
        
        for gasPos, fuel in stations:
            # when we exhaust our fuel tank then only add fuel
            while canGo < gasPos:
                # if no fuel left then we can not go any further
                if len(maxHeap) == 0:
                    return -1
                canGo += -heapq.heappop(maxHeap)
                refillCount += 1
            heapq.heappush(maxHeap, -fuel)
        
        # we crossed all gas stations 
        # now if we still didn't reach target then
        # add fuel until we reach
        while canGo < target:
            if len(maxHeap) == 0:
                return -1
            canGo += -heapq.heappop(maxHeap)
            refillCount += 1 
        
        return refillCount
# TC = O(nlog(n))
# SC = O(n)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minRefuelStops(target = 1, startFuel = 1, stations = []))
    print(sol.minRefuelStops(target = 100, startFuel = 1, stations = [[10,100]]))
    print(sol.minRefuelStops(target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]))
