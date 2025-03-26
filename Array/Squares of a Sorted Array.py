class Solution:
    def sortedSquares(self, nums):
        i, j = 0, len(nums)-1
        res = [0] * len(nums)
        k = j

        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                res[k] = nums[i]
                i += 1
            else:
                res[k] = nums[j]
                j -= 1

            # squaring element
            res[k] = res[k] * res[k]
            k -= 1

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.sortedSquares([-4, -1, 0, 3, 10]))
    print(sol.sortedSquares([-5,-3,-2,-1]))
        