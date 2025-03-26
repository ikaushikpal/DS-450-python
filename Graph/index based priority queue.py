class bidict(dict):
    def __init__(self, *args, **kwargs):
        super(bidict, self).__init__(*args, **kwargs)
        self.inverse = {}
        for key, value in self.items():
            self.inverse.setdefault(value,[]).append(key) 

    def __setitem__(self, key, value):
        if key in self:
            self.inverse[self[key]].remove(key) 
        super(bidict, self).__setitem__(key, value)
        self.inverse.setdefault(value,[]).append(key)        

    def __delitem__(self, key):
        self.inverse.setdefault(self[key],[]).remove(key)
        if self[key] in self.inverse and not self.inverse[self[key]]: 
            del self.inverse[self[key]]
        super(bidict, self).__delitem__(key)


class IPQ:
    def __init__(self):
        self.table = bidict()
        self.values = [None]
        self.position = [None]
        self.size = 1
        self.emptyLocation = []
        self.inverse = [None]

    def swim(self):
        currentIndex = self.size
        while currentIndex != 1 and self.values[self.position[currentIndex]] < self.values[self.position[currentIndex//2]]:
            self.position[currentIndex], self.position[currentIndex//2] = self.position[currentIndex//2], self.position[currentIndex]
            currentIndex = currentIndex // 2

    def sink(self):
        i = 1
        j = 2*i 
        while j < self.size:
            if j+1 <self.size and self.values[self.position[j]] < self.values[self.position[j+1]]:
                j = j+1
            
            if self.values[self.position[i]] >  self.values[self.position[j]]:
                self.position[i], self.position[j] = self.position[j], self.position[i]
            i *= 2
            j = 2*i 
        
    def insert(self, key, value):
        if len(self.emptyLocation) == 0:
            self.table[key] = self.size
            self.values.append(value)
            self.position.append(self.size)
            self.inverse.append(self.size)
            self.swim()
            self.size += 1
        else:
            location = self.emptyLocation.pop()
            self.table[key] = location
            self.values[1] = value
            self.inverse[location] = location
            self.position.append(location)
            self.swim()

    def pop(self):
        value = self.values[self.position[1]]
        index = self.inverse[self.position[1]]
        key = self.table.inverse[index][0]
        self.emptyLocation.append(index)
        self.size -= 1
        self.position[1] = self.position.pop()
        del self.table[key]
        self.sink()
        return key, value



ipq = IPQ()
ipq.insert('ram',10)
ipq.insert('sham',3)
ipq.insert('rahul',8)
ipq.insert('riya',15)
ipq.insert('roni',2)

x = ipq.pop()
print(x)
ipq.insert('lalu', 1)
print(ipq.pop())