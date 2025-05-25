# You are given an array(arr) of N number
# You have to select three indices i, j, k following this condition ->
# 0 <= i < j < k < N

# Two numbers X and Y as defined as:
# X = arr[i] ^ arr[i + 1] ^...^ arr[j - 1]
# Y = arr[j] ^ arr[j + 1] ^...^ arr[k]

# You have to print the number of triplets where X is equal to Y.


# Constraint
# 1 <= N <= 1000
# 0 <= arr[i] <= 10^9


from typing import List


class Solution:
    def solve(self, arr: List[int]) -> int:
        N = len(arr)
        ans = 0

        for i in range(N):
            xor = arr[i]

            for k in range(i + 1, N):
                xor ^= arr[k]

                if xor == 0:
                    ans += k - i
        return ans
# Time Complexity: O(N^2)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.solve([1, 3, 2, 5, 7, 2, 7, 5, 6, 4]))
