def findPrims(n:int)->None:
    arr = [0] * (n+1)

    for i in range(2, n+1, 1):
        if arr[i] == 0: # if it not a prime multiple or not marked yet
            for j in range(i*i, n+1, i):
                arr[j] = 1
    
    for i in range(2, n+1, 1):
        if arr[i] == 0:
            print(i, end=', ')
    
    print()


if __name__ == '__main__':
    n = 50
    findPrims(n)