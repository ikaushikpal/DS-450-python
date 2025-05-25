# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.


# Example 1:
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

# Example 2:
# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.
 

# Constraints:
# n == ratings.length
# 1 <= n <= 2 * 104
# 0 <= ratings[i] <= 2 * 104


from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # using slope algorithm
        N = len(ratings)
        ans = 1
        i = 1

        while i < N:
            while i < N and ratings[i - 1] == ratings[i]:
                ans += 1
                i += 1

            up, down = 1, 1

            while i < N and ratings[i - 1] < ratings[i]:
                i += 1
                up += 1
                ans += up

            while i < N and ratings[i - 1] > ratings[i]:
                i += 1
                down += 1
                ans += down
            
            if up > 1 and up < down:
                ans += down - up 
        return ans




if __name__ == '__main__':
    sol = Solution()
    print(sol.candy(ratings = [1,0,2]))
    print(sol.candy(ratings = [1,2,2]))