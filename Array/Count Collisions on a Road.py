class Solution:
    def countCollisions(self, directions: str) -> int:
        directions = list(directions)
        ans = 0
        for i in range(len(directions)):
            if directions[i] == 'L' and i > 0:
                if directions[i - 1] == 'S':
                    directions[i] = 'S'
                    ans += 1
                
            elif directions[i] == 'R' and i < len(directions)-1:
                if directions[i + 1] == 'S':
                    ans += 1
                    
                elif directions[i + 1] == 'L':
                    directions[i] = 'S'
                    directions[i + 1] = 'S'
                    ans += 2                
            
        return ans


print(Solution().countCollisions("LLRLRLLSLRLLSLSSSS"))
print(Solution().countCollisions("RLRSLL"))
print(Solution().countCollisions("LLRR"))