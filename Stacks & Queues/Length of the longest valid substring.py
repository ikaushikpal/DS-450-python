from  collections import  deque


def findMaxLength(string):
    n = len(string)
    stack = deque()
    stack.append(-1)
    count = 0
 
    for i in range(n):
        if string[i] == '(':
            stack.append(i)

        else:  
            if len(stack) != 0:
                stack.pop()

            # Check if this length formed with base of
            # current valid substring is more than max
            # so far
            if len(stack) != 0:
                count = max(count, i - stack[-1])

            # If stack is empty. push current index as
            # base for next valid substring (if any)
            else:
                stack.append(i)
    return count


def findMaxLengthConstant(string):
    # Variables for left and right counter.
    # maxlength to store the maximum length found so far
    left = 0
    right = 0
    maxlength = 0
    n = len(string)
    # Iterating the string from left to right
    for i in range(n):
 
        # If "(" is encountered,
        # then left counter is incremented
        # else right counter is incremented
        if (string[i] == '('):
            left += 1
        else:
            right += 1
 
        # Whenever left is equal to right, it signifies
        # that the subsequence is valid and
        if (left == right):
            maxlength = max(maxlength, 2 * right)
 
        # Reseting the counters when the subsequence
        # becomes invalid
        elif (right > left):
            left = right = 0
 
    left = right = 0
 
    # Iterating the string from right to left
    for i in range(n - 1, -1, -1):
 
        # If "(" is encountered,
        # then left counter is incremented
        # else right counter is incremented
        if (string[i] == '('):
            left += 1
        else:
            right += 1
 
        # Whenever left is equal to right, it signifies
        # that the subsequence is valid and
        if (left == right):
            maxlength = max(maxlength, 2 * left)
 
        # Reseting the counters when the subsequence
        # becomes invalid
        elif (left > right):
            left = right = 0

    return maxlength



string = '()(()))))'
s1 = '((()()()()(((())'
res = findMaxLengthConstant(s1)
print(res)