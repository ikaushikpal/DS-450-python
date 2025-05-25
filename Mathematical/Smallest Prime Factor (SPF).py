class Solution:
    def smallestPrimeFactor(self, N):
        spf = [i for i in range(N + 1)]

        i = 2
        while i * i <= N:
            if spf[i] == i:
                for j in range(i*i, N + 1, i):
                    if spf[j] == j:
                        spf[j] = i
            i += 1
        
        ans = []
        i = N
        while i != spf[i]:
            x = spf[i]
            ans.append(x)
            i = i // x
        ans.append(spf[i])
        return ans
# Time Complexity: O(Nlog(logN) + logN)   


if __name__ == '__main__':
    sol = Solution()
    print(sol.smallestPrimeFactor(45))