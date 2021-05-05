from collections import deque


# Expression may contain ‘+‘, ‘*‘, ‘–‘ and ‘/‘ operators
def checkRedundancy(string):
    stack = deque()
    operators = ['+', '-', '/', '*']

    for char in string:
        if char == '(':
            stack.append(0)

        elif char == ')':
            count = stack.pop()
            if count == 0:
                return True
        
        elif char in operators:
            stack[-1] += 1
    return False


if __name__ == "__main__":
    s1 = '((a+b))'
    s2 = '(a+(b)/c)'
    s3 = '(a+b*(c-d))'

    print(checkRedundancy(s1))
    print(checkRedundancy(s2))
    print(checkRedundancy(s3))
    print(checkRedundancy('(((a+b))+c)'))
    print(checkRedundancy('(a+((b*c)+c))'))

