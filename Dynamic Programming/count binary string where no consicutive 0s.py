# same as Consecutive 1's not allowed
# just there instead of 0s 1s but output will be same

# lets say n=3
# so binary strings = 2^3 = 8

# 000 not allowed
# 001 not allowed
# 010
# 011
# 100 not allowed
# 101
# 110
# 111

#  so output : 5


def countStrings(n):
    if n==0: return 0 # if n=0 then no string can be formed

    zeros = ones = 1 # for base length of 1

    for i in range(2, n+1):
        newZeros = ones
        newOnes = ones + zeros

        zeros = newZeros
        ones = newOnes
    
    return zeros + ones


if __name__ == "__main__":
    n = 3
    print(countStrings(n))