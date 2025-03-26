from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        N = len(pref)
        arr = [pref[0]]
        continues = pref[0]
        for i in range(1, N):
            arr.append(pref[i] ^ continues)
            continues ^= arr[-1]
        return arr