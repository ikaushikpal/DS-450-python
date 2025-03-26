# You are given N elements, you can remove any two elements from the list, note their sum, and add the sum to the list. Repeat these steps while there is more than a single element in the list. The task is to minimize the sum of these chosen sums.

 
# Example 1:
# Input:
# N = 4
# arr[] = {1, 4, 7, 10}

# Output:
# 39

# Explanation:
# Choose 1 and 4, Sum = 1 + 4 = 5.
# arr[] = {5, 7, 10} 
# Choose 5 and 7, Sum = 5 + (5 + 7) = 17.
# arr[] = {12, 10} 
# Choose 12 and 10, Sum = 17 + (12 + 10) = 39.
# arr[] = {22}
 

# Example 2:

# Input:
# N = 5
# arr[] = {1, 3, 7, 5, 6}

# Output:
# 48


import heapq


class Solution:
    def minimizeSum(self, N, minHeap):
        heapq.heapify(minHeap)
        ans = 0
        
        while len(minHeap) > 1:
            val1 = heapq.heappop(minHeap)
            val2 = heapq.heappop(minHeap)
            ans += val1 + val2
            
            heapq.heappush(minHeap, val1 + val2)
                            
        return ans
# Time Complexity: O(NlogN)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimizeSum(4, [1, 4, 7, 10]))
    print(sol.minimizeSum(5, [1, 3, 7, 5, 6]))