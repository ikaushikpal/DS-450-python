class Solution:
    def countAsterisks(self, s: str) -> int:
        arr = s.split('|')
        count = 0
        for i in range(0, len(arr), 2):
            count += arr[i].count('*')
        
        return count


sol = Solution()
print(sol.countAsterisks("l|*e*et|c**o|*de|"))
print(sol.countAsterisks("iamprogrammer"))
print(sol.countAsterisks("yo|uar|e**|b|e***au|tifu|l"))