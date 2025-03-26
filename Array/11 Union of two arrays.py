class Solution:
    def doUnion(self, a, n, b, m):
        set1 = set(a)
        set2 = set(b)

        set1 = set1.union(set2)
        return len(set1)
