# Given an array of integers, sort the array (in descending order) according to count of set bits in binary representation of array elements. 

# Note: For integers having same number of set bits in their binary representation, sort according to their position in the original array i.e., a stable sort.

# Example 1:

# Input: 
# arr[] = {5, 2, 3, 9, 4, 6, 7, 15, 32};
# Output:
# 15 7 5 3 9 6 2 4 32
# Explanation:
# The integers in their binary
# representation are:
# 15 - 1111
# 7  - 0111
# 5  - 0101
# 3  - 0011
# 9  - 1001
# 6  - 0110
# 2  - 0010
# 4  - 0100
# 32 - 10000
# hence the non-increasing sorted order is:
# {15}, {7}, {5, 3, 9, 6}, {2, 4, 32}
 

# Example 2:
# Input: 
# arr[] = {1, 2, 3, 4, 5, 6};
# Output: 
# 3 5 6 1 2 4
# Explanation:
# 3  - 0011
# 5  - 0101
# 6  - 0110
# 1  - 0001
# 2  - 0010
# 4  - 0100
# hence the non-increasing sorted order is
# {3, 5, 6}, {1, 2, 4}



from itertools import chain


class Solution:
    def sortBySetBitCount(self, arr, n):
        def countSetBits(num):
            count = 0
            while num:
                num = num & (num - 1)
                count += 1
            return count

        arr.sort(key = countSetBits, reverse = True)
        print(arr)
# Time Complexity : O(nlogn)
# Space Complexity : O(1)


class Solution:
    def sortBySetBitCount(self, arr, n):
        def countSetBits(num):
            count = 0
            while num:
                num = num & (num - 1)
                count += 1
            return count

        # arr elements in int32
        bucket = [[] for _ in range(32)]
        for val in arr:
            index = countSetBits(val)
            bucket[index].append(val)
        
        ans = list(chain(*bucket[::-1]))
        print(ans)
        arr[:] = ans
# Time Complexity : O(n)
# Space Complexity : O(32) = O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.sortBySetBitCount([5, 2, 3, 9, 4, 6, 7, 15, 32], 9))