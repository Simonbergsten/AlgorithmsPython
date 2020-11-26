from collections import deque

"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to
the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
Follow up:
Could you do get and put in O(1) time complexity?

"""


class LRUCache:

    def __init__(self, capacity):
        self.c = capacity
        self.m = dict()
        self.deq = deque()

    def get(self, key):
        if key in self.m:
            value = self.m[key]
            self.deq.remove(key)
            self.deq.append(key)
            return value
        else:
            return -1

    def put(self, key, value):
        if key not in self.m:
            if len(self.deq) == self.c:
                oldest = self.deq.popleft()
                del self.m[oldest]
        else:
            self.deq.remove(key)

        self.m[key] = value
        self.deq.append(key)


b = LRUCache(2)
b.put(1,1)
b.put(2,2)
b.get(1)
b.put(3,3)
b.get(2)
b.put(4,4)
b.get(1)
b.get(3)
print(b.get(4))


