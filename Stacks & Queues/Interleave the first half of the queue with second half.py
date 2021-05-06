from collections import deque


def interleaveQueue(queue):
    stack = deque()
    n = len(queue)

    for _ in range(n//2):
        stack.append(queue.popleft())
    
    for _ in range(n//2):
        queue.append(stack.pop())

    for _ in range(n//2):
        popped_item = queue.popleft()
        queue.append(popped_item)
    
    for _ in range(n//2):
        stack.append(queue.popleft())
    
    for _ in range(n//2):
        stack_pop = stack.pop()
        queue_pop = queue.popleft()

        queue.append(stack_pop)
        queue.append(queue_pop)



if __name__ == '__main__':
    q = deque([1, 2, 3, 4, 5, 6])
    interleaveQueue(q)

    for val in q:
        print(val, end=' ')
    print()
