from collections import defaultdict, OrderedDict


class Node:
    def __init__(self, data, hash_value):
        self.data = data
        self.hashKey = hash_value
        self.prev = None
        self.next = None


class DLL:
    def __init__(self, maxLength):
        self.maxLength = maxLength
        self.len = 0
        self.LRU_ptr = None
        self.MRU_ptr = None

    def pushPage(self, data, hash_key):
        newNode = Node(data, hash_key)
        preHash = None

        if self.MRU_ptr == None:
            self.MRU_ptr = self.LRU_ptr = newNode
            self.len += 1

        else:
            if self.len == self.maxLength:
                preHash = self.popPage()
            else:
                self.len += 1

            if self.MRU_ptr != None:
                newNode.next = self.MRU_ptr
                self.MRU_ptr.prev = newNode
                self.MRU_ptr = newNode
            else:
                self.MRU_ptr = self.LRU_ptr = newNode

        return newNode, preHash

    def popPage(self):
        preNode = self.LRU_ptr.prev
        tempHash = self.LRU_ptr.hashKey
        t = self.LRU_ptr

        self.LRU_ptr.prev = None
        if preNode != None:
            preNode.next = None
            self.LRU_ptr = preNode
        else:
            self.MRU_ptr = self.LRU_ptr = None

        del t
        return tempHash

    def updatePage(self, address):
        currentNode = address
        if self.len == 1 or self.MRU_ptr == currentNode:
            return currentNode

        prevNode = currentNode.prev
        if currentNode != self.LRU_ptr:
            nextNode = currentNode.next

            currentNode.prev = currentNode.next = None
            prevNode.next = nextNode
            nextNode.prev = prevNode
        else:
            prevNode.next = None
            self.LRU_ptr = prevNode

        currentNode.next = self.MRU_ptr
        self.MRU_ptr.prev = currentNode
        self.MRU_ptr = currentNode


class LRUCache:
    def __init__(self, capacity):
        self.cache = DLL(capacity)
        self.hashMap = defaultdict(lambda: None)

    def get(self, key):
        nodeAddress = self.hashMap[key]

        if nodeAddress != None:
            self.cache.updatePage(nodeAddress)
            return nodeAddress.data

        else:
            del self.hashMap[key]
            return -1

    def set(self, key, value):
        nodeAddress = self.hashMap[key]

        if nodeAddress == None:
            newNode, prevHash = self.cache.pushPage(value, key)
            self.hashMap[key] = newNode
            if prevHash != None:
                del self.hashMap[prevHash]

        else:
            self.cache.updatePage(nodeAddress)


class LRUCache2:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def set(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


if __name__ == "__main__":
    lru = LRUCache(2)
    lru.set(1, 2)
    lru.set(2, 3)
    lru.set(1, 5)
    lru.set(4, 5)

    print(lru.get(4))
    lru.set(1, 2)
    print(lru.get(3))
