class Solution:
    #Heapify function to maintain heap property.
    def heapify(self, arr, N, parent):
        left = 2 * parent + 1
        right = 2 * parent + 2
        largest = parent
        
        if left < N and arr[left] > arr[largest]:
            largest = left
        
        if right < N and arr[right] > arr[largest]:
            largest = right
        
        if largest != parent:
            arr[largest], arr[parent] = arr[parent], arr[largest]
            self.heapify(arr, N, largest)

    #Function to build a Heap from array.
    def buildHeap(self, arr, N):
        for i in range((N << 1) - 1, -1, -1):
            self.heapify(arr, N, i)

    def sink(self, arr, N):
        parent = 0
        child = 2 * parent

        while child < N:
            if child + 2 < N:
                child += 1 if arr[child+1] > arr[child+2] else 2
            else:
                child += 1

            if arr[parent] < arr[child]:
                arr[parent], arr[child] = arr[child], arr[parent]
                parent = child
                child = 2 * parent
            else:
                break

    def pop(self, arr, N):
        poppedVal = arr[0]
        arr[0] = arr[N-1]
        self.sink(arr, N-1)
        arr[N-1] = poppedVal

    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, N):
        self.buildHeap(arr, N)

        for i in range(N-1):
            self.pop(arr, N-i)
# Time Complexity : O(NlogN)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.HeapSort([4, 1, 3, 9, 7], 5))