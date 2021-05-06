from queue import Queue
from collections import deque


# iterative using emplicit stack
def rev2(q):
    s = deque()
    while q.empty() == False:
        s.append(q.get())
    
    while len(s):
        q.put(s.pop())
    
    return q


# using system stack
def rev(q):
    if q.qsize() > 0:
        x = q.get()
        q = rev(q)
        q.put(x)
        
    return q


q = Queue(maxsize=6)
for i in range(1, 6):
    q.put(i)

q = rev(q)
