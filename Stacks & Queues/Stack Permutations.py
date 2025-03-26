from collections import deque


def checkStackPermutation(pushed, popped, n):
    if n == 0:
        return True
    
    stack = deque()
    # stack.append(pushed[0])
    push_ptr = 0
    pop_ptr = 0

    while pop_ptr < n and push_ptr < n:
        if len(stack) == 0:
            stack.append(pushed[push_ptr])
            push_ptr += 1

        if stack[-1] != popped[pop_ptr]:
            stack.append(pushed[push_ptr])
            push_ptr += 1
        else:
            stack.pop()
            pop_ptr += 1
    
    # while pop_ptr < n:
    #     if stack[-1] != popped[pop_ptr]:
    #         return False
    #     else:
    #         stack.pop()
    #     pop_ptr += 1
    
    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    push = [1, 2, 3, 4, 5]
    pop  = [4, 5, 3, 2, 1]
    n    = len(push)


    res = checkStackPermutation(push, pop, n)
    print(res)
