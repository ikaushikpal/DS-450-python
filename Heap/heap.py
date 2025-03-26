class Heap:
    def __init__(self, minHeap=True):
        self.FLAG = minHeap
        self.arr = []

    def peek(self):
        return self.arr[0]
    
    def swim(self):
        child = len(self.arr) - 1
        parent = (child - 1) // 2

        while parent >= 0 and ((not self.FLAG and self.arr[child] > self.arr[parent])
                               or
                               ((self.FLAG and self.arr[child] < self.arr[parent]))):
            self.arr[parent], self.arr[child] = self.arr[child], self.arr[parent]
            child = parent
            parent = (child - 1) << 1

    def push(self, val):
        self.arr.append(val)
        self.swim()

    def findChild(self, parent):
        child = 2 * parent
        if 2 * parent + 2 < len(self.arr):
            if self.FLAG:
                child += 1 if self.arr[child+1] < self.arr[child+2] else 2
            else:
                child += 1 if self.arr[child+1] > self.arr[child+2] else 2
        else:
            child += 1

    def sink(self):
        parent = 0
        child = 2 * parent + 1

        while child < len(self.arr):
            child = self.findChild()

            if self.arr[parent] > self.arr[child]:
                self.arr[parent], self.arr[child] = self.arr[child], self.arr[parent]
                parent = child
            else:
                break

    def pop(self):
        poppedVal = self.arr[0]
        self.arr[0] = self.arr.pop()
        self.sink()
        return poppedVal

    def maxHeapify(self, parent):
        left = 2 * parent + 1
        right = 2 * parent + 2
        largest = parent
        
        if left < len(self.arr) and self.arr[left] > self.arr[largest]:
            largest = left
        
        if right < len(self.arr) and self.arr[right] > self.arr[largest]:
            largest = right
        
        if largest != parent:
            self.arr[largest], self.arr[parent] = self.arr[parent], self.arr[largest]
            self.maxHeapify(largest)

    def minHeapify(self, parent):
        left = 2 * parent + 1
        right = 2 * parent + 2
        minimum = parent
        
        if left < len(self.arr) and self.arr[left] < self.arr[minimum]:
            minimum = left
        
        if right < len(self.arr) and self.arr[right] < self.arr[minimum]:
            minimum = right
        
        if minimum != parent:
            self.arr[minimum], self.arr[parent] = self.arr[parent], self.arr[minimum]
            self.minHeapify(minimum)      

    def heapify(self):
        for i in range((len(self.arr)<< 1) - 1, -1, -1):
            if self.FLAG:
                self.minHeapify(i)
            else:
                self.maxHeapify(i)


if __name__ == '__main__':
    h = Heap()
    h.push(10)
    h.push(20)
    h.push(0)
    h.push(-0.5)
    print(h.pop())
    print(h.pop())
