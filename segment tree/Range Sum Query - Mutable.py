from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.segmentTree = [0] * (4 * len(nums))
        self.nums = nums

        leftRange = 0
        rightRange = len(nums) - 1
        self.build(0, leftRange, rightRange)

    def build(self, index, leftRange, rightRange):
        if leftRange == rightRange:
            self.segmentTree[index] = self.nums[leftRange]
        else:
            mid = (leftRange + rightRange) // 2
            left = self.build(2*index+1, leftRange, mid)
            right = self.build(2*index+2, mid+1, rightRange)

            self.segmentTree[index] = left + right

        return self.segmentTree[index]

    def update(self, index: int, val: int) -> None:
        if 0<=index<len(self.nums):
            self.updateHelper(0, 0, len(self.nums)-1, index, val)

    def updateHelper(self, index, leftRange, rightRange, targetIndex, val):
        # check if current node is target node
        if leftRange == rightRange:
            self.segmentTree[index] = val
        else:
            mid = (leftRange + rightRange) // 2

            left = self.segmentTree[2*index+1]
            right = self.segmentTree[2*index+2]

            # check if target node on left side
            if targetIndex <= mid:
                left = self.updateHelper(2*index+1, leftRange, mid, targetIndex, val)
            else:
                right = self.updateHelper(2*index+2, mid+1, rightRange, targetIndex, val)

            self.segmentTree[index] = left + right

        return self.segmentTree[index]

    def sumRange(self, left: int, right: int) -> int:
        return self.sumRangeHelper(0, 0, len(self.nums)-1, left, right)

    def sumRangeHelper(self, index, low, high, targetLeft, targetRight):
        if high < targetLeft or low > targetRight:
            return 0
            
        if low >= targetLeft and high <= targetRight:
            return self.segmentTree[index]

        leftIndex, rightIndex = 2*index+1, 2*index+2
        mid = (low + high) // 2

        left = self.sumRangeHelper(leftIndex, low, mid, targetLeft, targetRight)
        right = self.sumRangeHelper(rightIndex, mid+1, high, targetLeft, targetRight)

        return left + right


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


if __name__ == '__main__':
    sol = NumArray([9, -8])
    print(sol.update(0, 3))
    print(sol.sumRange(1, 1))
    print(sol.sumRange(0, 1))
    print(sol.update(1, -3))
    print(sol.sumRange(0, 1))
