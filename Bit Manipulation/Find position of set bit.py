class Solution:
    def findPosition(self, num):
        binaryEq = bin(num)
        pos = -1
        loc = 1

        for i in range(len(binaryEq)-1, 1, -1):
            if pos==-1 and binaryEq[i] == '1':
                pos = loc

            elif pos != -1 and binaryEq[i] == '1':
                return -1

            loc += 1

        return pos



if __name__ == '__main__':
    sol = Solution()
    print(sol.findPosition(5))
