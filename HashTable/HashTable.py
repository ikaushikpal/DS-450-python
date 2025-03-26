import math
import random


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, initialSize = 8, max_lambda=0.75):
        self.__max_lambda = max_lambda
        self.__size = initialSize
        self.__hash = [None] * self.__size
        self.__loadFactor = 0
        self.__counts = 0

    def set(self, key, value):
        initialHash = self.__h1(key)

        newNode = Node(key, value)
        if self.__hash[initialHash] == None:
            self.__hash[initialHash] = newNode
            self.__counts += 1

        else: # colision
            # lets first check if same is 

            for i in range(self.__size):
                newHash = (initialHash + i * self.__h2(key)) % self.__size

                if self.__hash[newHash] == None:
                    self.__hash[newHash] = Node(key, value)
                    self.__counts += 1
                    break

                elif self.__hash[newHash].key == key:
                    self.__hash[newHash].value = value
                    break

        self.__calculateLoadfactor()

        if self.__loadFactor >= self.__max_lambda:
            self.__rehash()

    def get(self, key):
        initialHash = self.__h1(key)

        for i in range(self.__size):
            newHash = (initialHash + i * self.__h2(key)) % self.__size

            if self.__hash[newHash] and self.__hash[newHash].key == key:
                return self.__hash[newHash].value

        raise KeyError(f"{key} does not exist in hashTable")

    def __containsUtil(self, key):
        initialHash = self.__h1(key)

        for i in range(self.__size):
            newHash = (initialHash + i * self.__h2(key)) % self.__size

            if self.__hash[newHash] and self.__hash[newHash].key == key:
                return newHash
        
        return None

    def contains(self, key):
        return True if self.__containsUtil(key) else False

    def __calculateLoadfactor(self):
        self.__loadFactor = self.__counts / self.__size

    def __rehash(self):
        old_size = self.__size
        old_hash = self.__hash
        
        self.__size = 2*old_size
        self.__hash = [None] * self.__size
        self.__counts = 0

        for address in old_hash:
            if address != None:
                self.set(address.key, address.value)

        self.__calculateLoadfactor()

    def __h1(self, key):
        CONST = 0.6180339887498949
        baseHash = hash(key)

        return math.floor(self.__size * ((baseHash * CONST) % 1))


    def __h2(self, key):
        baseHash = hash(key)
        tot = 0

        while baseHash:
            r1 = r2 = 0
            r1 = baseHash % 10
            baseHash //= 10

            if baseHash:
                r2 = baseHash % 10
                baseHash //= 10
            
            tot += (10*r2 + r1)
        
        return tot % self.__size

    def clear(self):
        self.__max_lambda = 0.75
        self.__size = 8
        self.__hash = [None] * self.__size
        self.__loadFactor = 0
        self.__counts = 0

    def copy(self):
        ht = HashTable()

        ht.__max_lambda = self.__max_lambda
        ht.__size = self.__size
        ht.__hash = self.__hash.copy()
        ht.__loadFactor = self.__loadFactor
        ht.__counts = self.__counts

        return ht

    def pop(self, key):
        if self.__counts == 0:
            raise KeyError("hashTable is empty")

        index = self.__containsUtil(key)
        if index == None:
            raise KeyError(f"{key} does not exist in hashTable")

        else:
            poppedValue = self.__hash[index].value

            self.__hash[index] = None
            self.__counts -= 1
            self.__calculateLoadfactor()

            return poppedValue

    def popitem(self):
        while True:
            index = math.floor(random.random() * (self.__size))
            if self.__hash[index] != None:
                ret = self.__hash[index].key, self.__hash[index].value

                self.__hash[index] = None
                self.__counts -= 1
                self.__calculateLoadfactor()

                return ret  

    def keys(self):
        for node in self.__hash:
            if node != None:
                yield node.key
    
    def values(self):
        for node in self.__hash:
            if node != None:
                yield node.value

    def items(self):
        for node in self.__hash:
            if node != None:
                yield (node.key, node.value)

    def __len__(self):
        return self.__counts
    
    def __iter__(self):
        return self.keys()

    def __contains__(self, key):
        return self.contains(key)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.set(key, value)
    
    def __delitem__(self, key):
        self.pop(key)

    def __str__(self):
        return f"hash table object with {self.__counts} keys"

if __name__ == '__main__':
    h = HashTable()
    h[10] = 100
    print(h[10])

    h[20] = 200
    print(h[20])

    h[10] = 300
    print(h[10])

    print(h[10] < h[20])
    h[20] = 300

    print(h[10] == h[20])