class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        if s == target:
            return True

        N = len(s)
        countS1 = s.count('1')
        countS0 = N - countS1

        if countS0 == N:
            return False

        countT1 = target.count('1')
        countT0 = N - countT1

        if countT0 == N:
            return False

        if countT1 > 0 and countS0 == 0:
            return False

        return True
