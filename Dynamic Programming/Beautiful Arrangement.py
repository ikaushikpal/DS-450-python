# Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

# perm[i] is divisible by i.
# i is divisible by perm[i].
# Given an integer n, return the number of the beautiful arrangements that you can construct.

 

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: 
# The first beautiful arrangement is [1,2]:
#     - perm[1] = 1 is divisible by i = 1
#     - perm[2] = 2 is divisible by i = 2
# The second beautiful arrangement is [2,1]:
#     - perm[1] = 2 is divisible by i = 1
#     - i = 2 is divisible by perm[2] = 1


# Example 2:
# Input: n = 1
# Output: 1


class Solution:
    def permutation(self, pos, visited, n):
        if pos == 0:
            return 1

        if visited in self.memo:
            return self.memo[visited]

        count = 0
        for i in range(1, n+1):
            # check if already used
            if visited & (1 << i):
                continue

            # check if i is divisible by pos
            if i % pos == 0 or pos % i == 0:
                count += self.permutation(pos-1, visited | (1 << i), n)
        
        self.memo[visited] = count
        return count

    def countArrangement(self, n: int) -> int:
        self.memo = {}
        return self.permutation(n, 0, n)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countArrangement(2))
    print(sol.countArrangement(1))
    print(sol.countArrangement(4))