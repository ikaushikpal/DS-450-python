def countBinaryString(n):
    if n==0: return 0

    zeros = ones = 1

    for i in range(2, n+1):
        newZeros = ones
        newOnes = ones + zeros

        ones = newOnes
        zeros = newZeros
    
    return ones + zeros
    

def arrageBuildings(n):
    oneSide = countBinaryString(n)
    return oneSide * oneSide


if __name__ == '__main__':
    n = 3
    print(arrageBuildings(n))