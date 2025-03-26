# Input: nums = ["102","473","251","814"], queries = [[1,1],[2,3],[4,2],[1,2]]
# Output: [2,2,1,0]
# Explanation:
# 1. After trimming to the last digit, nums = ["2","3","1","4"]. The smallest number is 1 at index 2.
# 2. Trimmed to the last 3 digits, nums is unchanged. The 2nd smallest number is 251 at index 2.
# 3. Trimmed to the last 2 digits, nums = ["02","73","51","14"]. The 4th smallest number is 73.
# 4. Trimmed to the last 2 digits, the smallest number is 2 at index 0.
#    Note that the trimmed number "02" is evaluated as 2.



from typing import List
import heapq


class Solution:
    # def kthSmallest(self, arr, l, r, k):
    #     if k > 0 and k <= r - l + 1:
    #         pos = self.partition(arr, l, r)

    #         if (pos - l == k - 1):
    #             return arr[pos][1]
    #         elif (pos - l > k - 1):
    #             return self.kthSmallest(arr, l, pos - 1, k)
    #         else:
    #             return self.kthSmallest(arr, pos + 1, r, k - pos + l - 1)

    #     return float('inf')
    
    # def partition(self, arr, l, r):
    #     x = arr[r][0]
    #     i = l
    #     for j in range(l, r):
    #         if (arr[j][0] <= x):
    #             arr[i], arr[j] = arr[j], arr[i]
    #             i += 1
    #     arr[i], arr[r] = arr[r], arr[i]
    #     return i


    def kthSmallest(self, arr, n, k):
        pq = []
        for i in range(k):
            heapq.heappush(pq, arr[i])
            heapq._heapify_max(pq)
            
        for i in range(k, n):
            if arr[i] < pq[0]:
                heapq.heappop(pq)

                heapq.heappush(pq, arr[i])
                heapq._heapify_max(pq)

        return pq[0]

    def removeTrim(self, nums, trim):
        return [(int(num[: -trim - 1 : -1][::-1]), i) for i, num in enumerate(nums)]

    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        tq = {}
        res = []
        maxTrim = len(nums[0])

        for query in queries:
            k, trim = query
            trim = min(trim, maxTrim)

            if trim not in tq:
                tq[trim] = self.removeTrim(nums, trim)

            res.append(self.kthSmallest(arr=tq[trim], n = len(tq[trim]), k=k)[1])
        return res


if __name__ == '__main__':
    sol = Solution()
    # print(sol.smallestTrimmedNumbers(nums = ["102","473","251","814"], queries = [[1,1],[2,3],[4,2],[1,2]]))
    print(sol.smallestTrimmedNumbers(["64333639502","65953866768","17845691654","87148775908","58954177897","70439926174","48059986638","47548857440","18418180516","06364956881","01866627626","36824890579","14672385151","71207752868"], 
[[9,4],[6,1],[3,8],[12,9],[11,4],[4,9],[2,7],[10,3],[13,1],[13,1],[6,1],[5,10]]))