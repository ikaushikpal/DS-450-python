# Given N friends, each one can remain single or can be paired up with some other friend. Each friend can be paired only once. Find out the total number of ways in which friends can remain single or can be paired up.
# Note: Since answer can be very large, return your answer mod 10^9+7.


# Example 1:

# Input:N = 3

# Output: 4

# Explanation:
# {1}, {2}, {3} : All single
# {1}, {2,3} : 2 and 3 paired but 1 is single.
# {1,2}, {3} : 1 and 2 are paired but 3 is single.
# {1,3}, {2} : 1 and 3 are paired but 2 is single.
# Note that {1,2} and {2,1} are considered same. (Meaning No permutations)

class Memo:
    def helper(self, n):
        if n == 1 or n == 0:
            return 1
        
        if n in self.memo:
            return self.memo[n] 
        
        self.memo[n] = self.helper(n-1) + (n-1) * self.helper(n-2)
        return self.memo[n]

    def countFriendsPairings(self, n):
        self.memo = {}
        return self.helper(n)


class Solution:
    def countFriendsPairings(self, n):
        if n <= 1:
            return n

        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        MOD = 10**9 + 7

        for i in range(2, n+1):
            dp[i] = (dp[i-1] + (i-1)*dp[i-2]) % MOD
        
        return dp[n]


if __name__ == '__main__':
    n = 4
    print(Solution().countFriendsPairings(n))
    print(Memo().countFriendsPairings(n))