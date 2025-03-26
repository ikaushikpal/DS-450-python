# A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

# Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

 
# Example 1:
# Input: arr = [3,5,1]
# Output: true
# Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.


# Example 2:
# Input: arr = [1,2,4]
# Output: false
# Explanation: There is no way to reorder the elements to obtain an arithmetic progression.


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        N = len(arr)
        maxx = max(arr)
        minn = min(arr)
        
        d = (maxx - minn) / (N - 1)
        a0 = minn
        elements = set(arr)
        
        for i in range(1, N):
            a = a0 + i * d
            if a not in elements:
                return False
        return True
# Time Complexity: O(N)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.canMakeArithmeticProgression([3,5,1]))
    print(sol.canMakeArithmeticProgression([1,2,4]))