import heapq


class Stack():
    def __init__(self):
        self.__heap = []
        self.timer = 10000
        super().__init__()

    def push(self, value):
        heapq.heappush(self.__heap, (self.timer, value))
        self.timer -= 1
    
    def pop(self):
        if len(self.__heap) == 0:
            return None

        _, value = heapq.heappop(self.__heap)
        return value
    
    def top(self):
        if len(self.__heap) == 0:
            return None

        _, value = heapq.heappop(self.__heap)
        heapq.heappush(self.__heap, (self.timer, value))
        return value


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.pop()
    
    s.push(3)
    s.push(4)
    s.pop()
    s.top()