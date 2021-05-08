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


if __name__ == '__main__':
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    n = len(arr)
    k = 3

    res = minimumSubArray(arr, n, k)
    print(res)
        