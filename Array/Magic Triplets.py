# Given an array of size n, a triplet (a[i], a[j], a[k]) is called a Magic Triplet if a[i] < a[j] < a[k] and i < j < k.  Count the number of magic triplets in a given array.
 

# Example 1:
# Input: arr = [3, 2, 1]
# Output: 0
# Explanation: There is no magic triplet.


# Example 2:
# Input: arr = [1, 2, 3, 4]
# Output: 4
# Explanation: Fours magic triplets are 
# (1, 2, 3), (1, 2, 4), (1, 3, 4) and 
# (2, 3, 4).


class Solution:
    def countTriplets(self, nums):
        ans = 0
        N = len(nums)

        for i in range(1, N-1):
            left = sum(1 for j in range(i) if nums[j] < nums[i])
            right = sum(1 for j in range(i+1, N) if nums[i] < nums[j])
            ans += left * right
        return ans
# Time Complexity: O(n^2)
# Space Complexity: O(1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.countTriplets([3, 2, 1]))
    print(sol.countTriplets([1, 2, 3, 4]))
