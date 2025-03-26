# Given a sorted array A[] of N positive integers having all the numbers occurring exactly twice, except for one number which will occur only once. Find the number occurring only once.

# Example 1:

# Input:
# N = 5
# A = {1, 1, 2, 5, 5}
# Output: 2
# Explanation: 
# Since 2 occurs once, while
# other numbers occur twice, 
# 2 is the answer.
# Example 2:

# Input:
# N = 7
# A = {2, 2, 5, 5, 20, 30, 30}
# Output: 20
# Explanation:
# Since 20 occurs once, while
# other numbers occur twice, 
# 20 is the answer.


class Solution:
    def search(self, A, N):
        low, high = 0, N-1

        while low <= high:
            mid = (low + high) // 2
            
            if (mid==0 or A[mid-1] != A[mid]) and (mid==N-1 or A[mid] != A[mid+1]):
                return A[mid]
            
            if mid & 1:
                if A[mid] == A[mid-1]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if A[mid] == A[mid-1]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.search([1, 1, 2, 5, 5], 5))
    print(sol.search([2, 2, 5, 5, 20, 30, 30], 7))