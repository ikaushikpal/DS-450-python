from collections import Counter
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
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        d = Disjoint(n)
        for u, v in edges:
            d.union(u, v)
            d.union(v, u)
        
        for u, v in edges:
            d.union(u, v)
            d.union(v, u)
            
        # [2, 6, -4, -1, 2, 2, -2]
        comp = Counter()
        for i in range(n):
            val = d.array[i]
            if val >= 0:
                comp[val] += 1
            else:
                comp[i] += 1
        print(d.array)
        print(comp)
        count = 0
        for key, value in comp.items():
            count += (n - value) * value
        
        return count // 2

sol = Solution()
print(sol.countPairs(11, [[5,0],[1,0],[10,7],[9,8],[7,2],[1,3],[0,2],[8,5],[4,6],[4,2]]))