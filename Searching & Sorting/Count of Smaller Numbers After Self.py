# You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

 

# Example 1:
# Input: nums = [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.


# Example 2:
# Input: nums = [-1]
# Output: [0]


# Example 3:
# Input: nums = [-1,-1]
# Output: [0,0]


from typing import List


class Solution:
    def merge(self, left, mid, high, arr):
        temp = []
        i, j = left, mid + 1
        while i <= mid and j <= high:
            leftVal, leftIndex = arr[i]
            rightVal, rightIndex = arr[j]

            if leftVal > rightVal:
                self.ans[leftIndex] += high - j + 1
                temp.append((leftVal, leftIndex))
                i += 1
            else:
                temp.append((rightVal, rightIndex))
                j += 1

        while i <= mid:
            temp.append(arr[i])
            i += 1
        
        while j <= high:
            temp.append(arr[j])
            j += 1
        
        arr[left : high + 1] = temp
        
    def mergeSort(self, low, high, arr):
        if low < high:
            mid = (low + high) // 2
            self.mergeSort(low, mid, arr)
            self.mergeSort(mid + 1, high, arr)
            self.merge(low, mid, high, arr)

    def countSmaller(self, nums: List[int]) -> List[int]:
        # approach :
        # need to use merge sort, in reverse order
        # first make a numsIndex = (num, index)
        # when merging, need to do something different
        # like arr1[i] > arr2[j]
        # this means arr1[i] is greater than arr2[j] and because actual index of arr2 is on the right,
        # so if arr1[i] > arr2[j] then we can safely say that there exist at least one element on the right side of arr1[i]
        # that is less than arr1[i]
        arr = [(num, i) for i, num in enumerate(nums)]
        self.ans = [0] * len(nums)
        self.mergeSort(0, len(arr)-1, arr)
        return self.ans
# Time Complexity: O(NlogN)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countSmaller([5,2,6,1]))
    print(sol.countSmaller([-1]))
    print(sol.countSmaller([-1,-1]))