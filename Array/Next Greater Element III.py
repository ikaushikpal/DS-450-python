class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n < 0:
            return -1

        num = list(str(n))
        if len(num) == 1:
            return -1
        
        # finding the swaping index
        swapIndex = -1
        for i in range(len(num)-2, -1, -1):
            if num[i] < num[i+1]:
                swapIndex = i
                break
                
        if swapIndex == -1:
            return -1
        
        # now swap with num[swapIndex] and smallest greater element than num[swapIndex]
        smallestGreaterIndex = -1
        for i in range(len(num)-1, swapIndex, -1):
            if num[i] > num[swapIndex]:
                smallestGreaterIndex = i
                break
        
        num[swapIndex], num[smallestGreaterIndex] = num[smallestGreaterIndex], num[swapIndex]
        newNum = num[:swapIndex+1] + num[swapIndex+1:][::-1]

        newNumInt = int(''.join(newNum))

        if 1<=newNumInt<=((1<<31) - 1):
            return newNumInt
        else:
            return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.nextGreaterElement(6537421))
