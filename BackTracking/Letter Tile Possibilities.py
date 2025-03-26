# You have n  tiles, where each tile has one letter tiles[i] printed on it.

# Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

# Example 1:
# Input: tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".


# Example 2:
# Input: tiles = "AAABBC"
# Output: 188


# Example 3:
# Input: tiles = "V"
# Output: 1


class Solution:
    def helper(self, tiles, visited, path):
        if path not in self.ans:
            self.ans.add(path)

        for i in range(len(tiles)):
            if not visited[i]:
                visited[i] = True
                self.helper(tiles, visited, path + tiles[i])
                visited[i] = False
            
    def numTilePossibilities(self, tiles: str) -> int:
        self.ans = set()
        self.helper(tiles, [False] * len(tiles), "")
        # -1 because we do not consider empty string
        return len(self.ans) - 1
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)


if __name__ == '__main__':
    sol = Solution()
    print(sol.numTilePossibilities("AAB"))
    print(sol.numTilePossibilities("AAABBC"))
    print(sol.numTilePossibilities("V"))