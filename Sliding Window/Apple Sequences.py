# There is a string of size n containing only 'A' and 'O'. 'A' stands for Apple, and 'O' stands for Orange. We have m number of spells, each spell allows us to convert an orange into an apple.

# Find the longest sequence of apples you can make, given a string and the value of m.


# Example 1:
# Input:
# N = 5
# M = 1
# arr[] = 'AAOAO'
# Output: 4 
# Explanation: Changing the orange at 
# 3rd position into an apple gives 
# us the maximum possible answer.


# Example 2:
# Input:
# N = 5
# M = 1
# arr = 'AOOAO'
# Output: 2
# Explanation: Changing any orange into 
# an apple will give us a sequence 
# of length 2.


class Solution:
    def appleSequences(self, n, m, arr):
        start = ans = 0

        for end in range(n):
            if arr[end] == 'O':
                m -= 1
            
            while m < 0 and start < n:
                if arr[start] == 'O':
                    m += 1
                start += 1
            
            window = end - start + 1
            ans = max(ans, window)
        return ans
# Time Complexity: O(n)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.appleSequences(5, 1, 'AAOAO'))
    print(sol.appleSequences(5, 1, 'AOOAO'))