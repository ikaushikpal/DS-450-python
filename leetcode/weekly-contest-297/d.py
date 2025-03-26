from typing import Counter, List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        hashC = Counter(ideas)
        count = 0

        for i in range(len(ideas)):
            lword = ideas[i]
            for j in range(len(ideas)):
                if i == j:
                    continue
                rword = ideas[j]
                lwordNew = rword[0] + lword[1:]
                rwordNew = lword[0] + rword[1:]

                if lwordNew not in hashC and rwordNew not in hashC:
                    count += 1
        
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.distinctNames(ideas = ["coffee","donuts","time","toffee"]))