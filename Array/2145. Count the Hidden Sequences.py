# You are given a 0-indexed array of n integers differences, which describes the differences between each pair of consecutive integers of a hidden sequence of length (n + 1). More formally, call the hidden sequence hidden, then we have that differences[i] = hidden[i + 1] - hidden[i].

# You are further given two integers lower and upper that describe the inclusive range of values [lower, upper] that the hidden sequence can contain.

# For example, given differences = [1, -3, 4], lower = 1, upper = 6, the hidden sequence is a sequence of length 4 whose elements are in between 1 and 6 (inclusive).
# [3, 4, 1, 5] and [4, 5, 2, 6] are possible hidden sequences.
# [5, 6, 3, 7] is not possible since it contains an element greater than 6.
# [1, 2, 3, 4] is not possible since the differences are not correct.
# Return the number of possible hidden sequences there are. If there are no possible sequences, return 0.

# Example 1:
# Input: differences = [1,-3,4], lower = 1, upper = 6
# Output: 2
# Explanation: The possible hidden sequences are:
# - [3, 4, 1, 5]
# - [4, 5, 2, 6]
# Thus, we return 2.

# Example 2:
# Input: differences = [3,-4,5,1,-2], lower = -4, upper = 5
# Output: 4
# Explanation: The possible hidden sequences are:
# - [-3, 0, -4, 1, 2, 0]
# - [-2, 1, -3, 2, 3, 1]
# - [-1, 2, -2, 3, 4, 2]
# - [0, 3, -1, 4, 5, 3]
# Thus, we return 4.

# Example 3:
# Input: differences = [4,-7,2], lower = 3, upper = 6
# Output: 0
# Explanation: There are no possible hidden sequences. Thus, we return 0.

from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # Initialize variables to track the minimum and maximum values
        # that the array elements can reach as we apply the differences.
        min_range = max_range = value = 0

        # Traverse the differences array to simulate building the original array.
        for diff in differences:
            # Calculate the next value in the array by adding the current difference.
            next_value = value + diff

            # Update the minimum value seen so far.
            if next_value < min_range:
                min_range = next_value

            # Update the maximum value seen so far.
            if next_value > max_range:
                max_range = next_value

            # Move to the next value.
            value = next_value
        
        # The total range of values that the reconstructed array can take.
        diff_range = max_range - min_range

        # The range of values allowed by the given bounds.
        provided_range = upper - lower

        # If the difference in values exceeds the allowed range, it's impossible to build such an array.
        if diff_range > provided_range:
            return 0
        
        # Otherwise, count the number of valid starting points (initial values)
        # that would keep the whole array within the bounds.
        return provided_range - diff_range + 1

# Time Complexity: O(N)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfArrays(differences = [1,-3,4], lower = 1, upper = 6))
    print(sol.numberOfArrays(differences = [3,-4,5,1,-2], lower = -4, upper = 5))
    print(sol.numberOfArrays(differences = [4,-7,2], lower = 3, upper = 6))