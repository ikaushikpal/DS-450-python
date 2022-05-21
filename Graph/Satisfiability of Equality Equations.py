# You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

# Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.

 

# Example 1:
# Input: equations = ["a==b","b!=a"]
# Output: false
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
# There is no way to assign the variables to satisfy both equations.



# Example 2:
# Input: equations = ["b==a","a==b"]
# Output: true
# Explanation: We could assign a = 1 and b = 1 to satisfy both equations.


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
    def equationsPossible(self, equations: List[str]) -> bool:
        d = Disjoint(256)
        
        for equation in equations:
            a, op, b = equation[0], equation[1:3], equation[-1]
            if op == '==':
                d.union(ord(a), ord(b))
        
        for equation in equations:
            a, op, b = equation[0], equation[1:3], equation[-1]
            if op == '!=':
                x = d.find(ord(a))[0]
                y = d.find(ord(b))[0]
                if x == y:
                    return False
                
        return True
# Time Complexity = O(N)
# Space Complexity = O(256)
# Where N is the number of equations.
# The space complexity is due to the Disjoint data structure.
# amortized time complexity of disjoint set = O(1) 


if __name__ == '__main__':
    equations = ["a==b","b!=a"]
    print(Solution().equationsPossible(equations))

    equations = ["b==a","a==b"]
    print(Solution().equationsPossible(equations))