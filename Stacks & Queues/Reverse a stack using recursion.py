def insertBottom(stack, val):
    if len(stack) == 0:
        stack.append(val)
        return stack

    x = stack.pop()
    stack = insertBottom(stack, val)
    stack.append(x)
    return stack

# O(n**2)
def reverseStack(stack):
    if len(stack):
        x = stack.pop()
        stack = reverseStack(stack)
        stack = insertBottom(stack, x)
        return stack
    else:
        return []


if __name__ == "__main__":
    stack = [1, 2, 3, 4, 5, 6]
    res = reverseStack(stack)
    print(res)