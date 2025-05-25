# Given two arrays, val[] and wt[], representing the values and weights of items, and an integer capacity representing the maximum weight a knapsack can hold, determine the maximum total value that can be achieved by putting items in the knapsack. You are allowed to break items into fractions if necessary.
# Return the maximum value as a double, rounded to 6 decimal places.

# Examples :

# Example 1:
# Input: val[] = [60, 100, 120], wt[] = [10, 20, 30], capacity = 50
# Output: 240.000000
# Explanation: Take the item with value 60 and weight 10, value 100 and weight 20 and split the third item with value 120 and weight 30, to fit it into weight 20. so it becomes (120/30)*20=80, so the total value becomes 60+100+80.0=240.0 Thus, total maximum value of item we can have is 240.00 from the given capacity of sack.

# Example 2:
# Input: val[] = [60, 100], wt[] = [10, 20], capacity = 50
# Output: 160.000000
# Explanation: Take both the items completely, without breaking. Total maximum value of item we can have is 160.00 from the given capacity of sack.

# Example 3:
# Input: val[] = [10, 20, 30], wt[] = [5, 10, 15], capacity = 100
# Output: 60.000000
# Explanation: In this case, the knapsack capacity exceeds the combined weight of all items (5 + 10 + 15 = 30). Therefore, we can take all items completely, yielding a total maximum value of 10 + 20 + 30 = 60.000000.

# Constraints:
# 1 <= val.size=wt.size <= 105
# 1 <= capacity <= 109
# 1 <= val[i], wt[i] <= 104


class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, val, wt, capacity):
        # per weight basis valued items
        items = [(v / w, v, w) for v, w in zip(val, wt)]
        items.sort(reverse=True)

        ans = i = 0
        while i < len(val) and capacity:
            _, v, w = items[i]

            if w <= capacity:
                ans += v
                capacity -= w
            else:
                frac = v / w * capacity
                ans += frac
                break
            i += 1
        return ans


# Time Complexity: O(NlogN)
# Space Complexity: o(N)


if __name__ == "__main__":
    sol = Solution()
    print(sol.fractionalknapsack([60, 100, 120], [10, 20, 30], 50))
    print(sol.fractionalknapsack([60, 100], [10, 20], 50))
    print(sol.fractionalknapsack([10, 20, 30], [5, 10, 15], 100))
