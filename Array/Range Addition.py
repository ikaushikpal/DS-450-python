class Solution:
    def __init__(self, n):
        self.nums = [0] * (n+1)

    def update(self, startIndex, endIndex, value):
        self.nums[startIndex] += value
        self.nums[endIndex + 1] += -value
    
    def print(self):
        prefixSum = 0

        for i in range(len(self.nums)):
            prefixSum += self.nums[i]
            self.nums[i] = prefixSum
        
        print(self.nums[:-1])



if __name__ == '__main__':
    sol = Solution(5)
    sol.update(1, 3, 2)
    sol.update(2, 4, 3)
    sol.update(0, 2, -2)

    sol.print()