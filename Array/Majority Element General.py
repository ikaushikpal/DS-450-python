# if k value is high then its much much better to use hashmap solution

class Solution:
    def majorityElementGeneral(self, nums, k):
        values = self.majorityElementGeneralHelper(nums, k)
        counts = [0] * len(values)

        for num in nums:
            for j in range(len(values)):
                if values[j] == num:
                    counts[j] += 1

        res = []
        floor_value = len(nums) // k
        
        for j in range(len(values)):
            if counts[j] > floor_value:
                res.append(values[j])

        return res

    def majorityElementGeneralHelper(self, nums, k):
        values = [0] * (k-1)
        counts = [0] * (k-1)

        for i in range(len(nums)):
            MATCHED = False

            for j in range(k-1):
                if nums[i] == values[j]:
                    counts[j] += 1
                    MATCHED = True
                    break

            if not MATCHED:
                ANY_COUNT_ZERO = False

                for j in range(k-1):
                    if counts[j] == 0:
                        values[j], counts[j] = nums[i], 1
                        ANY_COUNT_ZERO = True
                        break

                if not ANY_COUNT_ZERO:
                    for j in range(k-1):
                        counts[j] -= 1
        
        # return list(set(values))
        return values


if __name__ == '__main__':
    sol = Solution()
    print(sol.majorityElementGeneral([3, 1, 2, 2, 1, 2, 3, 3], 4))