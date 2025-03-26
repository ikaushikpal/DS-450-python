from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            x = list(str(num))
            x = list(map(int, x))
            ans.extend(x)
        return ans


sol = Solution()
print(sol.separateDigits([13,25,83,77]))
print(sol.separateDigits([7,1,3,9]))
