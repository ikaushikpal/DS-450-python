from collections import deque


def nextGreaterRight(arr: list) -> list:
    stack = deque()
    result = []

    for i in range(len(arr)-1, -1, -1):
        if len(stack) == 0:
            result.append(-1)

        elif stack[-1] > arr[i]:
            result.append(stack[-1])

        else:
            while len(stack) and stack[-1] <= arr[i]:
                stack.pop()

            if len(stack) == 0:
                result.append(-1)
            else:
                result.append(stack[-1])
        stack.append(arr[i])

    return result[::-1]


if __name__ == "__main__":
    arr1 = [1, 3, 2, 4]
    arr2 = [1, 3, 0, 0, 1, 2, 4]
    res = nextGreaterRight(arr2)
    print(res)
