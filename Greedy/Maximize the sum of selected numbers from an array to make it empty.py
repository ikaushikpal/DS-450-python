# Given a array of N numbers, we need to maximize the sum of selected numbers. At each step, you need to select a number Ai, delete one occurrence of Ai-1 (if exists), and Ai each from the array. Repeat these steps until the array gets empty. The problem is to maximize the sum of the selected numbers.


# Example 1:
# Input : arr[ ] = {1, 2, 2, 2, 3, 4}
# Output : 10
# Explanation:
# We select 4, so 4 and 3 are deleted leaving us with {1,2,2,2}.
# Then we select 2, so 2 & 1 are deleted. We are left with{2,2}.
# We select 2 in next two steps, thus the sum is 4+2+2+2=10.


# Example 2:
# Input : arr[ ] = {1, 2, 3} 
# Output :  4
# Explanation: We select 3, so 3 and 2 are deleted leaving us with {1}. Then we select 1, 0 doesn't exist so we delete 1. thus the sum is 3+1=4.


# from collections import Counter


# class Solution:
    
#     def maximizeSum (self,arr, n) : 
#         hashMap = Counter(arr)
#         total = 0
#         for key in sorted(hashMap.keys(), reverse = True):
#             if hashMap[key] > 0:
#                 total += hashMap[key] * key
#                 hashMap[key - 1] -= hashMap[key]
#         return total
# Time Complexity: O(nlogn)
# Space Complexity: O(n)


class Solution:
    def maximizeSum (self,arr, n) : 
        prevEle, prevFreq = float('inf'), 0
        total, i = 0, n - 1
        
        while i >= 0:
            ele, freq = arr[i], 0
            
            while i >= 0 and arr[i] == ele:
                i -= 1
                freq += 1
            
            if ele + 1 == prevEle:
                extra = max(freq - prevFreq, 0)
                total += extra * ele
                prevFreq = extra
            else:
                total += freq * ele
                prevFreq = freq
                
            prevEle = ele
        return total
# Time Complexity: O(n)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximizeSum([1, 2, 2, 2, 3, 4], 6))
    print(sol.maximizeSum([1, 2, 3], 3))
    print(sol.maximizeSum(sorted([9, 15, 9, 3, 8, 4, 6, 17, 7, 11, 17, 7, 3, 18, 13, 9, 7, 12, 2, 8]), 20))
