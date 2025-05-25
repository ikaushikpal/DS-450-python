# Given an array arr of N integers, the task is to replace each element of the array by its rank in the array. The rank of an element is defined as the distance between the element with the first element of the array when the array is arranged in ascending order. If two or more are same in the array then their rank is also the same as the rank of the first occurrence of the element. 

# Example 1:
# Input:
# N = 6
# arr = [20, 15, 26, 2, 98, 6]
# Output:
# 4, 3, 5, 1, 6, 2
# Explanation:
# After sorting, array becomes {2,6,15,20,26,98}
# Rank(2) = 1 (at index 0) 
# Rank(6) = 2 (at index 1) 
# Rank(15) = 3 (at index 2) 
# Rank(20) = 4 (at index 3) and so on..

# Example 2:
# Input:
# N = 4
# arr = [2, 2, 1, 6]
# Output:
# 2, 2, 1, 3
# Explanation:
# After sorting, array becomes {1, 2, 2, 6}
# Rank(1) = 1 (at index 0) 
# Rank(2) = 2 (at index 1) 
# Rank(2) = 2 (at index 2) 
# Rank(6) = 3 (at index 3)
# Rank(6) = 3 because rank after 2 is 3 as rank 
# of same element remains same and for next element 
# increases by 1.
# Your Task:
# Complete the function int replaceWithRank(), which takes integer N  and an array of N integers as input and returns the list in which element at each position of original array is replaced by the rank of that element.

# Expected Time Complexity: O(N * logN)
# Expected Auxiliary Space: O(N)

# Constraints:
# 1 <= N <= 105
# 1 <= arr[i] <= 109


class Solution:
    def replaceWithRank(self, N, arr):
        items = [(val, i) for i, val in enumerate(arr)]
        items.sort()

        ans = [0] * len(arr)
        new_index = 1
        for i, (val, old_index) in enumerate(items):

            if i - 1 >= 0 and items[i - 1][0] == items[i][0]:
                # if having same value then not increasing rank
                new_index -= 1
            ans[old_index] = new_index
            new_index += 1
        return ans
# Time Complexity: O(NlogN)
# Space Complexity: o(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.replaceWithRank(6, [20, 15, 26, 2, 98, 6]))
    print(sol.replaceWithRank(4, [2, 2, 1, 6]))