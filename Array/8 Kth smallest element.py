import heapq


class Solution:
    def kthSmallest(self, arr, l, r, k):
        maxHeap = []
        for i in range(len(arr)):
            heapq.heappush(maxHeap, arr[i])

        for i in range(k-1):
            heapq.heappop(maxHeap)

        return heapq.heappop(maxHeap)

    def kthSmallestV2(self, arr, l, r, k):
        maxHeap = []

        for val in arr:
            heapq.heappush(maxHeap, -val)
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return -maxHeap[0]


if __name__ == "__main__":
    arr = list(map(int, "7 10 4 20 15".split(' ')))
    n = len(arr)
    k = 4

    s = Solution()
    res = s.kthSmallestV2(arr, 0, n-1, k)
    print(res)
