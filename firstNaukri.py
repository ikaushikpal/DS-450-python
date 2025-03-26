def solve(arr, n):
    ans = 0
    MOD = 1000000007
    for i in range(31):
        countSetBits = 0

        for j in range(n):
            if arr[j] & (1 << i) :
                countSetBits += 1
 
        subset = (1 << countSetBits) - 1
        subset = subset * (1 << i)
        ans = (ans + subset) % MOD
    return ans % MOD


t = int(input())
for _ in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	print(solve(arr, n))