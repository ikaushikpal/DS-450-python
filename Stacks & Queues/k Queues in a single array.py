class KStacks():
    def __init__(self, k, capacity):
        self.nextAvailable = 0
        self.data = [0] * capacity
        self.front = [-1] * k
        self.rear = [-1] * k
        self.nextIndex = [i+1 for i in range(capacity)]
        self.nextIndex[capacity-1] = -1

    def isFull(self):
        return self.nextAvailable == -1
    
    def isEmpty(self, k):
        return self.front[k] == -1

    def enqueue(self, k, data):
        if self.isFull():
            return
        
        nextFree = self.nextIndex[self.nextAvailable]

        if self.isEmpty(k):
            self.front[k] = self.rear[k] = self.nextAvailable
        else:
            self.rear[k] = self.nextAvailable
            self.nextIndex[ self.front[k] ] = self.nextAvailable

        self.nextIndex[self.nextAvailable] = -1
        self.data[ self.nextAvailable ] = data
        self.nextAvailable = nextFree

    def dequeue(self, k):
        if self.isEmpty(k):
            return None
        
        fetch_index = self.front[k]
        ret_data = self.data[fetch_index]

        self.front[k] = self.nextIndex[fetch_index]
        self.nextIndex[fetch_index] = self.nextAvailable
        self.nextAvailable = fetch_index

        return ret_data

if __name__ == '__main__':
    k_stack = KStacks(3, 4)
    k_stack.enqueue(0, 10)
    k_stack.enqueue(1, 20)
    k_stack.enqueue(2, 30)
    k_stack.enqueue(0, 40)
    k_stack.enqueue(1, 50)

    k_stack.dequeue(0)
    k_stack.dequeue(1)

        
