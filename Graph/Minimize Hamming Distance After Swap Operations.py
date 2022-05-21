# You are given two integer arrays, source and target, both of length n. You are also given an array allowedSwaps where each allowedSwaps[i] = [ai, bi] indicates that you are allowed to swap the elements at index ai and index bi (0-indexed) of array source. Note that you can swap elements at a specific pair of indices multiple times and in any order.

# The Hamming distance of two arrays of the same length, source and target, is the number of positions where the elements are different. Formally, it is the number of indices i for 0 <= i <= n-1 where source[i] != target[i] (0-indexed).

# Return the minimum Hamming distance of source and target after performing any amount of swap operations on array source.

 

# Example 1:
# Input: source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
# Output: 1
# Explanation: source can be transformed the following way:
# - Swap indices 0 and 1: source = [2,1,3,4]
# - Swap indices 2 and 3: source = [2,1,4,3]
# The Hamming distance of source and target is 1 as they differ in 1 position: index 3.



# Example 2:
# Input: source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
# Output: 2
# Explanation: There are no allowed swaps.
# The Hamming distance of source and target is 2 as they differ in 2 positions: index 1 and index 2.



# Example 3:
# Input: source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
# Output: 0


from collections import defaultdict, Counter
from typing import List


class Disjoint:
    def __init__(self, n=0):
        self.n = n
        self.array = [-1] * self.n

    def add(self):
        self.array.append(-1)
        self.n += 1

    def find(self, n):
        if self.array[n] < 0:
            return (n,  -self.array[n])
        result = self.find(self.array[n])
        self.array[n] = result[0]
        return result
    
    def union(self, set1, set2):
        parent_of_set1, rank_of_set1 = self.find(set1)
        parent_of_set2, rank_of_set2 = self.find(set2)

        if parent_of_set1 == parent_of_set2:
            return False

        if rank_of_set1 > rank_of_set2:
            self.array[parent_of_set1] += self.array[parent_of_set2]
            self.array[parent_of_set2] = parent_of_set1
            
        else:
            self.array[parent_of_set2] += self.array[parent_of_set1]
            self.array[parent_of_set1] = parent_of_set2
        return True


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        if len(allowedSwaps) == 0:
            res = 0
            for ch1, ch2 in zip(source, target):
                if ch1 != ch2:
                    res += 1
            return res

        dsu = Disjoint(len(source))
        for u, v in allowedSwaps:
            dsu.union(u, v)
        
        clusteredIndex = defaultdict(set)

        for u, v in allowedSwaps:
            uParent = dsu.find(u)[0]
            vParent = dsu.find(v)[0]
            clusteredIndex[uParent].add(u)
            clusteredIndex[vParent].add(v)
        
        res = 0
        for u in clusteredIndex:
            t = Counter(source[i] for i in clusteredIndex[u])
            total = len(clusteredIndex[u])
      
            for i in clusteredIndex[u]:
                if target[i] in t:
                    if t[target[i]] > 0:
                        total -= 1
                    t[target[i]] -= 1
            
            res += total
        
        return res



if __name__ == '__main__':
    s = Solution()
    print(s.minimumHammingDistance(source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]))
    print(s.minimumHammingDistance(source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []))
    print(s.minimumHammingDistance(source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]))
    print(s.minimumHammingDistance([2,3,1], [1,2,2], [[0,2],[1,2]]))
