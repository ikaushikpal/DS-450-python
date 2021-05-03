from collections import deque


def nextSmallerLeft(arr: list, pseudo_index=-1) -> list:
    stack = deque()
    result = []

    for i in range(0, len(arr), 1):
        if len(stack) == 0:
            result.append(pseudo_index)

        elif arr[stack[-1]] > arr[i]:
            result.append(pseudo_index)

        else:
            while len(stack) and arr[stack[-1]] <= arr[i]:
                stack.pop()

            if len(stack) == 0:
                result.append(pseudo_index)
            else:
                result.append(i - stack[-1])
        stack.append(i)

    return result


def stockSpain(arr: list) -> list:
    return nextSmallerLeft(arr, 1)


if __name__ == '__main__':
    arr = [100, 80, 60, 70, 60, 75, 85]
    res = stockSpain(arr)
    print(res)
