class SegmentTree:
    def __init__(self, array):
        self.arrayLow, self.arrayHigh = 0, len(array)-1
        self.segmentTree = [0] * (4*len(array))
        self.lazy = [0] * (4*len(array))

        self.build(array, 0, self.arrayLow, self.arrayHigh)

    def build(self, array, segmentIndex, low, high):
        # if this is left node
        if low == high:
            self.segmentTree[segmentIndex] = array[low]
            return self.segmentTree[segmentIndex]
        
        mid = (low + high) // 2
        x = self.build(array, 2*segmentIndex+1, low, mid)
        y = self.build(array, 2*segmentIndex+2, mid+1, high)

        self.segmentTree[segmentIndex] = max(x, y)
        return self.segmentTree[segmentIndex]

    def lazyPropagator(self, segmentIndex, low, high):
        leftChildIndex = 2*segmentIndex + 1
        rightChildIndex = 2*segmentIndex + 2

        if self.lazy[segmentIndex]:
            # updating main segment tree
            lazyVal = self.lazy[segmentIndex]
            self.segmentTree[segmentIndex] += lazyVal

            # this is not a leaf node
            if low != high:
                self.lazy[leftChildIndex]  += lazyVal
                self.lazy[rightChildIndex] += lazyVal

            self.lazy[segmentIndex] = 0

    def update(self, index, value):
        if self.arrayLow<=index<=self.arrayHigh:
            self.updateHelper(0, self.arrayLow, self.arrayHigh, index, value)

    def updateHelper(self, segmentIndex, low, high, index, value):
        leftChildIndex = 2*segmentIndex + 1
        rightChildIndex = 2*segmentIndex + 2

        self.lazyPropagator(segmentIndex, low, high)

        if low == high:
            self.segmentTree[segmentIndex] = value
            return

        mid = (low + high) // 2
        # check if need to go left side
        if index <= mid:
            self.updateHelper(leftChildIndex, low, mid, index, value)
        else:
            self.updateHelper(rightChildIndex, mid+1, high, index, value)

        self.segmentTree[segmentIndex] = max(self.segmentTree[leftChildIndex], self.segmentTree[rightChildIndex])
    

    def updateRange(self, low, high, val):
        self.updateRangeHelper(0, self.arrayLow, self.arrayHigh, low, high, val)
    
    def updateRangeHelper(self, segmentIndex, low, high, targetLow, targetHigh, value):
        leftChildIndex = 2*segmentIndex + 1
        rightChildIndex = 2*segmentIndex + 2

        self.lazyPropagator(segmentIndex, low, high)

        # if current range does not lie in between range
        if high < targetLow or low > targetHigh:
            return float('-inf')
        
        # if current range perfectly lie in b/w range
        if targetLow <= low and high <= targetHigh:
            self.lazy[leftChildIndex] = self.lazy[rightChildIndex] = value
            self.segmentTree[segmentIndex] += value
            return self.segmentTree[segmentIndex]

        # if current range partially lie in b/w range
        mid = (low + high) // 2
        x = self.updateRangeHelper(leftChildIndex, low, mid, targetLow, targetHigh, value)
        y = self.updateRangeHelper(rightChildIndex, mid+1, high, targetLow, targetHigh, value)

        self.segmentTree[segmentIndex] = max(x, y)
        return self.segmentTree[segmentIndex]


    def maxRange(self, low, high):
        if low <= high and self.arrayLow <= low and high <= self.arrayHigh:
            return self.maxRangeHelper(0, self.arrayLow,self.arrayHigh, low, high)

    def maxRangeHelper(self, segmentIndex, low, high, targetLow, targetHigh):
        leftChildIndex = 2*segmentIndex + 1
        rightChildIndex = 2*segmentIndex + 2

        self.lazyPropagator(segmentIndex, low, high)

        # if current range does not lie in between range
        if high < targetLow or low > targetHigh:
            return float('-inf')
        
        # if current range perfectly lie in b/w range
        if targetLow <= low and high <= targetHigh:
            return self.segmentTree[segmentIndex]

        # if current range partially lie in b/w range
        mid = (low + high) // 2
        x = self.maxRangeHelper(leftChildIndex, low, mid, targetLow, targetHigh)
        y = self.maxRangeHelper(rightChildIndex, mid+1, high, targetLow, targetHigh)

        return max(x, y)


if __name__ == '__main__':
    seg = SegmentTree([1, 3, 5])
    
    print(seg.maxRange(1, 2))
    print(seg.maxRange(0, 2))

    print(seg.updateRange(0, 1, 10))
    print(seg.maxRange(1, 2))
    print(seg.maxRange(0, 2))

    print(seg.update(0, 100))
    print(seg.maxRange(1, 2))
    print(seg.maxRange(0, 2))

    print(seg.updateRange(0, 2, -70))
    print(seg.maxRange(1, 2))
    print(seg.maxRange(0, 2))
