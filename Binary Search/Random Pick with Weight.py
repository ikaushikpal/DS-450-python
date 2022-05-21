# You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

# You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

# For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
 


# Example 1:
# Input
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output
# [null,0]

# Explanation
# Solution solution = new Solution([1]);
# solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.


# Example 2:
# Input
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output
# [null,1,1,1,1,0]

# Explanation
# Solution solution = new Solution([1, 3]);
# solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 1
# solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

# Since this is a randomization problem, multiple answers are allowed.
# All of the following outputs can be considered correct:
# [null,1,1,1,1,0]
# [null,1,1,1,1,1]
# [null,1,1,1,0,0]
# [null,1,1,1,0,1]
# [null,1,0,1,0,0]
# ......
# and so on.



import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        # generating prefix sum
        # using prefix sum representing the probability of picking a number
        # lets say, w = [1, 2, 3]
        # |-|--|---|   line represents probability
        # 0 1  2   3   simple cumulative sum
        # this represents the probability of picking a number from 1 to 3
        # the higher the probability, higher the line length
        self.prefixSum = w
        for i in range(1, len(w)):
            self.prefixSum[i] += self.prefixSum[i - 1]
            
        self.minRange, self.maxRange = 1, self.prefixSum[-1]

    
    def findCeil(self, target):
        if target > self.prefixSum[-1]:
            return -1

        low, high = 0, len(self.prefixSum) - 1
        res = -1

        while low <= high:
            mid = (low+high)//2

            if self.prefixSum[mid] == target:
                return mid
            
            elif self.prefixSum[mid] < target:
                low = mid + 1       
            else:
                res = mid
                high = mid - 1

        return res
    
    def pickIndex(self) -> int:
        # generate a random number between 1 and the sum of all the weights(excluded)
        # now we need to find the index of the number that has the probability of the random number
        # because line length is proportional to the probability, as well as for the random index
        # so there is high probability that the random index lies in higher probability area

        # e.g. [1, 2, 3]
        # |-|--|---|   line represents probability
        # randomIndex can be 1, 2, 3, 4, 5, 6
        # out of these 1 lie in first segment, (2, 3) lie in second segment, (4, 5, 6) lie in third segment
        # so chances of getting 3 is 3/6, 2 is 2/6, 1 is 1/6

        # NOTE: here we are excluding last element from prefix sum, because ceil function will return -1 if target is greater than the last element
        # which is wrong
        randomIndex = random.randint(1, self.maxRange)
        return max(self.findCeil(randomIndex), 0)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()