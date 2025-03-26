class Solution:
    def solve(self, n, s, cost):
        ans = 0
        for i in range(2, n, 2):
            if i<n-1 and not ((s[i] == s[n-i+1] and s[i+1] == s[n-i]) or (s[i] == s[n-i] and s[i + 1] == s[n-i+1])):
                # indices.append([(i, n-i+1), (i+1, n-i), (i, n-1), (i+1, n-i+1)])
                ans += 1

        return ans


print(Solution().solve(4, 'bdbd', [1, 2, 3, 4]))
print(Solution().solve(8, 'abbacaaa', [1, 2, 3, 4, 2, 3, 0, 1]))
