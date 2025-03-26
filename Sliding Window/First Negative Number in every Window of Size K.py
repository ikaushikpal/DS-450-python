from collections import deque


def firstNegative(arr, n, k):
    result = []
    queue = deque()

    for i in range(k):
        if arr[i] < 0:
            queue.append(i)
    
    for i in range(k, n):
        if len(queue) == 0:
            result.append(0)
        else:
            result.append(arr[queue[0]])

            if queue[0] == i-k:
                queue.popleft()
        
        if arr[i] < 0:
            queue.append(i)
        
    if len(queue) == 0:
            result.append(0)
    else:
        result.append(arr[queue[0]])
        
    return result

def firstNegative2(arr, n, k):
    queue = deque()

    i = j = 0 
    while j < n:
        if arr[j] < 0:
            queue.append(j)
        
        if j -i +1 < k:
            j += 1
        else:
            if len(queue) == 0:
                print(0, end=' ')
            else:
                print(arr[queue[0]], end=' ')
                if queue[0] == i:
                    queue.popleft()
            i += 1
            j += 1
            

if __name__ == '__main__':
    arr = [12, -1, -7, 8, -15, 30, 16, 28]
    n = len(arr)
    k = 3

    res =firstNegative(arr, n, k)
    print(res)
    firstNegative2(arr, n, k)