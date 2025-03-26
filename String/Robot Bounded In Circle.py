class Solution:
    def rotate(self, times):
        for _ in range(times):
            sign = 1 if self.sp % 2 else -1
            # swap x and y
            self.dir_x, self.dir_y = self.dir_y * sign, self.dir_x * sign

            self.sp = (self.sp + 1) % 4
        
    def isRobotBounded(self, instructions: str) -> bool:
        # initalizing
        self.dir_x, self.dir_y = 0, 1
        self.sp = 0
        self.loc_x, self.loc_y = 0, 0
    
        count_rotation = 0

        for i in instructions:
            if i == 'G':
                self.rotate(count_rotation)
                
                count_rotation = 0
                self.loc_x += self.dir_x
                self.loc_y += self.dir_y
            else:
                if i == 'L':
                    count_rotation = (count_rotation+1) % 4
                else:
                    count_rotation = (count_rotation+3) % 4
                        
                
        if 'G' not in instructions[-1]:
                self.rotate(count_rotation)

        if (self.loc_x == 0 and self.loc_y == 0) or (self.sp != 0):
            return True
        else:
            return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.isRobotBounded("GGLLGG"))
    print(sol.isRobotBounded("GG"))
    print(sol.isRobotBounded("GL"))
    print(sol.isRobotBounded("GG"))
    print(sol.isRobotBounded("GLGLGLGL"))
        