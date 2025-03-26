class Solution:
    def maxHeapify(self, index, nums):
        left = 2*index + 1
        right = 2*index + 2
        largest = index

        if left < len(nums) and nums[left] > nums[largest]:
            largest = left
        
        if right < len(nums) and nums[right] > nums[largest]:
            largest = right
        
        if largest != index:
            nums[index], nums[largest] = nums[largest], nums[index]
            self.maxHeapify(largest, nums)

    def heapify(self, nums):
        for i in range(len(nums) << 1 - 1, -1, -1):
            self.maxHeapify(i, nums)

    def convertToMaxHeap(self, minHeap):
        self.heapify(minHeap)
        return minHeap


if __name__ == '__main__':
    sol = Solution()
    print(sol.convertToMaxHeap([3, 5, 9, 6, 8, 20, 10, 12, 18, 9]))