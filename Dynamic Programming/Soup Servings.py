# There are two types of soup: type A and type B. Initially, we have n ml of each type of soup. There are four kinds of operations:

# Serve 100 ml of soup A and 0 ml of soup B,
# Serve 75 ml of soup A and 25 ml of soup B,
# Serve 50 ml of soup A and 50 ml of soup B, and
# Serve 25 ml of soup A and 75 ml of soup B.
# When we serve some soup, we give it to someone, and we no longer have it. Each turn, we will choose from the four operations with an equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve as much as possible. We stop once we no longer have some quantity of both types of soup.

# Note that we do not have an operation where all 100 ml's of soup B are used first.

# Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time. Answers within 10-5 of the actual answer will be accepted.

 

# Example 1:
# Input: n = 50
# Output: 0.62500
# Explanation: If we choose the first two operations, A will become empty first.
# For the third operation, A and B will become empty at the same time.
# For the fourth operation, B will become empty first.
# So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.


# Example 2:
# Input: n = 100
# Output: 0.71875


import unittest


class Solution:
    dp = {}
    
    def helper(self, cupA, cupB):
        """
        Calculate the probability of reaching a certain state of liquid in Cup A and Cup B.

        Args:
            cupA (int): The current amount of liquid in Cup A.
            cupB (int): The current amount of liquid in Cup B.

        Returns:
            float: The probability of reaching the desired state of liquid.

        Notes:
            This function uses dynamic programming to calculate the probability of reaching a certain
            state of liquid in Cup A and Cup B. It recursively calls itself with different amounts of
            liquid removed from each cup, and then averages the results.

            If Cup A or Cup B is empty, the probability is 0. If Cup A and Cup B are both empty, the
            probability is 0.5. And if only cupA is empty then 1. If the state of liquid in Cup A and Cup B has already been calculated,
            the function returns the cached result.

            The calculated probability is then stored in the `self.dp` dictionary for future use.

            The function returns the final probability of reaching the desired state of liquid.

        """
        if cupA <= 0 and cupB > 0:
            return 1
        
        if cupA <= 0 and cupB <= 0:
            return 0.5
        
        if cupB <= 0:
            return 0
        
        if (cupA, cupB) in self.dp:
            return self.dp[(cupA, cupB)]
        
        res = 0
        for i in range(4):
            res += self.helper(cupA - (4 - i) * 25, cupB - i* 25)
            
        res = res / 4
        self.dp[(cupA, cupB)] = res
        return res
            
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1
        return self.helper(n, n)
# Time Complexity: O(200 * 200)
# Space Complexity: O(200 * 200)


class SolutionTests(unittest.TestCase):
    def setUp(self):
        """
        Set up the test case by initializing the `solution` instance variable with a new instance of the `Solution` class.
        """
        self.solution = Solution()

    def test_soupServings(self):
        # Add test cases for the soupServings function
        self.assertEqual(self.solution.soupServings(50), 0.62500)
        self.assertEqual(self.solution.soupServings(100), 0.71875)
        # Add more test cases...


if __name__ == "__main__":
    unittest.main()