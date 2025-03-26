# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

 
# Example 1:
# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
# Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.


# Example 2:
# Input: letters = ["c","f","j"], target = "c"
# Output: "f"
# Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.


# Example 3:
# Input: letters = ["x","x","y","y"], target = "z"
# Output: "x"
# Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].


from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        
        low, high = 0, len(letters) - 1
        ceilLetter = letters[0]
        
        while low <= high:
            mid = (low + high) >> 1
            
            if letters[mid] <= target:
                low = mid + 1
            else:
                ceilLetter = letters[mid]
                high = mid - 1
        return ceilLetter
# Time Complexity: O(log n)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.nextGreatestLetter(["c","f","j"], "a"))
    print(sol.nextGreatestLetter(["c","f","j"], "c"))
    print(sol.nextGreatestLetter(["x","x","y","y"], "z"))