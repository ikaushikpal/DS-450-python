# Given a positive integer n, generate all possible unique ways to represent n as sum of positive integers.
# Note: The generated output is printed without partitions. Each partition must be in decreasing order. Printing of all the partitions is done in reverse sorted order. 


# Example 1:
# Input: n = 3
# Output: 3 2 1 1 1 1
# Explanation: For n = 3, 
# {3}, {2, 1} and {1, 1, 1}.
 

# Example 2:
# Input: n = 4 
# Output: 4 3 1 2 2 2 1 1 1 1 1 1
# Explanation: For n = 4, 
# {4}, {3, 1}, {2, 2}, {2, 1, 1}, {1, 1, 1, 1}.


class Solution:
    def helper(self, n, prev, current):
        if n == 0:
            self.finalAns.append(current[:])
            return
        
        for i in range(min(prev, n), 0, -1):
            current.append(i)
            self.helper(n - i, i, current)
            current.pop()
            
    def UniquePartitions(self, n):
        self.finalAns = []
        self.helper(n, float('inf'), [])
        return self.finalAns
# Time Complexity: O(2^n)
# Space Complexity: O(n)


if __name__ == "__main__":
    sol = Solution()
    print(sol.UniquePartitions(3))
    print(sol.UniquePartitions(4))
