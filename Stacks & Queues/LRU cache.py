# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

 

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4

from collections import defaultdict, OrderedDict


class DLL:
    class Node:
        def __init__(self, key, data, left=None, right=None):
            self.key = key
            self.data = data
            self.left = left
            self.right = right

    def __init__(self):
        self.head = DLL.Node(None, None)
        self.tail = DLL.Node(None, None)
        self.head.right = self.tail
        self.tail.left = self.head
        self.len = 0
    
    def delete(self, node):
        leftNode, rightNode = node.left, node.right
        leftNode.right = rightNode
        rightNode.left = leftNode
        self.len -= 1
        key, value = node.key, node.data
        del node
        return (key, value)
    
    def deleteLast(self):
        return self.delete(self.tail.left)

    def insert(self, key, value):
        leftNode, rightNode = self.head, self.head.right
        newNode = DLL.Node(key, value, leftNode, rightNode)
        leftNode.right = newNode
        rightNode.left = newNode
        self.len += 1
        return newNode


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pages = DLL()
        self.hashMap = {}

    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1

        oldNode = self.hashMap[key]
        self.pages.delete(oldNode)
        newNode = self.pages.insert(key, oldNode.data)
        self.hashMap[key] = newNode
        return newNode.data
    
    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            node = self.hashMap[key]
            self.pages.delete(node)
            
        elif len(self.hashMap) == self.capacity:
            oldKey, _ = self.pages.deleteLast()
            del self.hashMap[oldKey]

        newNode = self.pages.insert(key, value)
        self.hashMap[key] = newNode

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
    lru = LRUCache(3)
    lru.set(1, 10)
    lru.set(3, 15)
    print(lru.get(1))
    lru.set(2, 12)
    print(lru.get(3))
    lru.set(4, 20)
    print(lru.get(2))
    print(lru.get(4))
    print(lru.get(1))
    lru.set(4, 25)

