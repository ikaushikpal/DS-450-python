# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

 

# Example 1:
# Input: n = 3, k = 3
# Output: "213"


# Example 2:
# Input: n = 4, k = 9
# Output: "2314"


# Example 3:
# Input: n = 3, k = 1
# Output: "123"


class Solution:
    def findFact(self, n):
        fact = 1
        for i in range(2, n+1):
            fact *= i
        return fact
    
    def getPermutation(self, n: int, k: int) -> str:
        # first find factorial of n-1
        fact = self.findFact(n - 1)
        # generate nums arr for n
        nums = [i for i in range(1, n+1)]
        value = 0
        # converting k(1-based) to 0-based
        k = k - 1
        
        while len(nums) > 1:
            # find the index of the number be next
            index = k // fact
            # add the number to the value
            value = value * 10 + nums[index]
            # map k value from n values to n-1 values
            k = k % fact
            # remove the number from the nums arr
            nums.pop(index)
            # update factorial to get (len(nums) - 1)!
            fact = fact // len(nums)
            
        # when len(nums) = 1, add the last number to the value
        value = value * 10 + nums[0]
        return str(value)
# Time Complexity: O(n*n)
# Space Complexity: O(n)


if __name__ == '__main__':
    sol = Solution()
    print(sol.getPermutation(3, 3))
    print(sol.getPermutation(4, 9))