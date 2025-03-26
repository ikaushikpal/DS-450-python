from collections import deque


def nextSmallerLeft(arr: list, pseudo_index=-1) -> list:
    stack = deque()
    result = []

    for i in range(0, len(arr), 1):
        if len(stack) == 0:
            result.append(pseudo_index)

        elif arr[stack[-1]] < arr[i]:
            result.append(stack[-1])

        else:
            while len(stack) and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if len(stack) == 0:
                result.append(pseudo_index)
            else:
                result.append(stack[-1])
        stack.append(i)

    return result


def nextSmallerRight(arr: list, pseudo_index=-1) -> list:
    stack = deque()
    result = []

    for i in range(len(arr)-1, -1, -1):
        if len(stack) == 0:
            result.append(pseudo_index)

        elif arr[stack[-1]] < arr[i]:
            result.append(stack[-1])

        else:
            while len(stack) and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if len(stack) == 0:
                result.append(pseudo_index)
            else:
                result.append(stack[-1])
        stack.append(i)

    return result[::-1]


def maximumArea(arr: list) -> int:
    n = len(arr)
    left = nextSmallerLeft(arr, -1)
    right = nextSmallerRight(arr, n)

    area = []
    for i in range(n):
        width = right[i] - left[i] - 1
        area.append(width * arr[i])

    return max(area)


def maximumAreaBinary(mat: list) -> int:
    m = len(mat)
    n = len(mat[0])
    hist = [0] * n
    max_area = 0

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                hist[j] = 0
            else:
                hist[j] += mat[i][j]

        max_area = max(max_area, maximumArea(hist))

    return max_area


if __name__ == '__main__':
    mat = [[0, 1, 1, 0], [1, 1, 1, 1], [
        1, 1, 1, 1], [1, 1, 0, 0]]

    res = maximumAreaBinary(mat)
    print(res)
