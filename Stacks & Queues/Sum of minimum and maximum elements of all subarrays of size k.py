from collections import deque

def minimumSubArray(arr, n, k):
    i = j = 0
    queue = deque()
    res = []

    while j < n:
        while len(queue) and arr[queue[-1]] > arr[j]:
            queue.pop()
        queue.append(j)

        if  j-i+1 < k:
            j += 1
        else:
            res.append(arr[queue[0]])
            if queue[0] == i:
                queue.popleft()
            
            i += 1
            j += 1
    
    return res

def maximumSubArray(arr, n, k):
    i = j = 0
    queue = deque()
    res = []

    while j < n:
        while len(queue) and arr[queue[-1]] < arr[j]:
            queue.pop()
        queue.append(j)

        if  j-i+1 < k:
            j += 1
        else:
            res.append(arr[queue[0]])
            if queue[0] == i:
                queue.popleft()
            
            i += 1
            j += 1
    
    return res

def min_max_subArray(arr, k, n):
    mini = minimumSubArray(arr, n, k)
    maxi = maximumSubArray(arr, n, k)

    tot = 0
    for i in range(n-k+1):
        tot += mini[i] + maxi[i]

    return tot
            

if __name__ == '__main__':
    arr = [2, 5, -1, 7, -3, -1, -2]
    k = 4
    n = len(arr)

    print(min_max_subArray(arr, k, n))
    