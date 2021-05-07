from collections import deque


def min_max_subArray(arr, k, n):
    min_q = deque()
    max_q = deque()

    total_sum = 0
    for i in range(k):
        if len(max_q) == 0 and len(min_q) == 0:
            max_q.append((i, arr[i]))
            min_q.append((i, arr[i]))
        
        elif arr[i] > max_q[-1][1]:
            max_q.append((i, arr[i]))
        elif arr[i] < min_q[-1][1]:
            min_q.append((i, arr[i]))

    total_sum += min_q[-1][1] + max_q[-1][1]

    for i in range(k, n):
        s_range = i-k+1

        minI = minVal = None
        if len(min_q) > 0:
            minI, minVal = min_q[0]

        if minI:
            if minI < s_range:
                min_q.popleft()

            if arr[i] < min_q[-1]:
                min_q.append((i, arr[i]))
            
            
                

            








if __name__ == '__main__':
    arr = [2, 5, -1, 7, -3, -1, -2]
    k = 4
    n = len(arr)