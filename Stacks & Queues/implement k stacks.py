class KStacks():   
    def __init__(self, k, n):
        self.data = [0] * n
        self.topOfStack = [-1] * k
        self.nextIndex = [i+1 for i in range(n)]
        self.nextIndex[n-1] = -1
        self.nextAvailable = 0
    
    def isFull(self):
        return self.nextAvailable == -1

    def push(self, k, value):
        if self.isFull() == False:
            free = self.nextIndex[self.nextAvailable]
            self.data[self.nextAvailable] = value
            self.nextIndex[self.nextAvailable] = self.topOfStack[k]
            self.topOfStack[k] = self.nextAvailable
            self.nextAvailable = free

    def pop(self, k):
        if self.isEmpty(k):
            return None
        
        index = self.topOfStack[k]
        value = self.data[index]
        self.topOfStack[k] = self.nextIndex[index]
        self.nextIndex[index] = self.nextAvailable
        self.nextAvailable = index
        
        return value
    
    def isEmpty(self, k):
        return self.topOfStack[k] == -1
    
    def top(self, k):
        if self.isEmpty(k):
            return None
        return self.data[self.topOfStack[k]]


if __name__ == '__main__':
    kstacks = KStacks(3, 5)

    kstacks.push(0, 10)       
    kstacks.push(2, 20)       
    kstacks.push(2, 200)       
    kstacks.push(1, 30)  
    kstacks.push(1, 300)  

    kstacks.pop(0)     
    kstacks.pop(1)     
    kstacks.pop(2)     
    kstacks.pop(0)     