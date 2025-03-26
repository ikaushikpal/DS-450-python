def leastPrimeFactors(n:int)->None:
    arr = [0] * (n+1)

    for i in range(2, n+1, 1):
        if arr[i] == 0: # if it not a prime multiple or not marked yet
            arr[i] = i
            for j in range(i*i, n+1, i):
                if arr[j] == 0:
                    arr[j] = i
    
    for i in range(2, n+1, 1):
        print(f"Least Prime factor of {i}: {arr[i]}")
    

if __name__ == '__main__':
    n = 50
    leastPrimeFactors(n)