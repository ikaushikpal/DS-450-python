from collections import deque


def hasConnections(mat, u, v):
    if mat[u][v] == 0:
        return False
    return True

def isCelebrity(mat, index):
    for i in range(len(mat)):
        if i != index and mat[index][i] != 0:
            return False
    
    for i in range(len(mat)):
        if i != index and mat[i][index] != 1:
            return False
    
    return True


def findCelebrity(mat):
    stack = deque()
    n = len(mat)

    for i in range(n):
        stack.append(i)
    
    # finding who can be celebrity and who not
    # if a knows b then a is not a celebrity
    # but it is not said that b is the celebrity
    while len(stack) > 1:
        v = stack.pop()
        u = stack.pop()

        connection = hasConnections(mat, u, v)
        if connection == False: # u do not know v then u may a celebrity
            stack.append(u)
        else:
            stack.append(v)
    
    potential_celebrity = stack.pop()
    if isCelebrity(mat, potential_celebrity):
        return potential_celebrity
    else:
        return None


MATRIX = [ [ 0, 1, 1, 1 ],
           [ 0, 0, 1, 1 ],
           [ 0, 0, 0, 0 ],
           [ 1, 0, 1, 0 ] ]

res = findCelebrity(MATRIX)
print(res)