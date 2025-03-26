def complement_1s(bit):
    return 0 if bit else 1


def solve(n, k):
    if n == 1 and k == 1:
        return 0
    
    if n > k:
        return solve(n-1, k)
    else:
        return complement_1s(solve(n-1, k-n+1))


N = 3
for i in range(1,(1<<(N-1))+1):
    print(solve(N, i), end=' ')