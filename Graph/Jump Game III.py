# Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

# Notice that you can not jump outside of the array at any time.

 
# Example 1:
# Input: arr = [4,2,3,0,3,1,2], start = 5
# Output: true
# Explanation: 
# All possible ways to reach at index 3 with value 0 are: 
# index 5 -> index 4 -> index 1 -> index 3 
# index 5 -> index 6 -> index 4 -> index 1 -> index 3 


# Example 2:
# Input: arr = [4,2,3,0,3,1,2], start = 0
# Output: true 
# Explanation: 
# One possible way to reach at index 3 with value 0 is: 
# index 0 -> index 4 -> index 1 -> index 3


# Example 3:
# Input: arr = [3,0,2,1,2], start = 2
# Output: false
# Explanation: There is no way to reach at index 1 with value 0.


from collections import deque
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if start < 0 or start >= len(arr):
            return False
        
        N = len(arr)
        queue = deque([start])
        visited = [False] * N
        visited[start] = True
        
        while queue:
            pos = queue.popleft()
            
            if arr[pos] == 0:
                return True
            
            leftPos, rightPos = pos - arr[pos], pos + arr[pos]
            
            if leftPos >= 0 and not visited[leftPos]:
                visited[leftPos] = True
                queue.append(pos - arr[pos])
                
            if rightPos < len(arr) and not visited[rightPos]:
                visited[rightPos] = True
                queue.append(pos+arr[pos])
                
        return False
# Time Complexity: O(N)
# Space Complexity: O(N)
# where N is the length of the array.


if __name__ == "__main__":
    arr = [4,2,3,0,3,1,2]
    start = 5
    print(Solution().canReach(arr, start))

    arr = [4,2,3,0,3,1,2]
    start = 0
    print(Solution().canReach(arr, start))

    arr = [3,0,2,1,2]
    start = 2
    print(Solution().canReach(arr, start))
