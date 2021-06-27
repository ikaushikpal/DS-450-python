class Solution:
    def __init__(self, weights, sum):
        self.weights = weights
        self.N = len(weights)
        self.visited = [False] * self.N
        self.targetSum = sum

    def generateSubsets(self):
        total = sum(self.weights)
        self.generateSubsetsUtil(0, 0, total)


    def generateSubsetsUtil(self, loc, currentSum, remainingSum):
        if currentSum == self.targetSum:
            self.printSubset()
            return

        if currentSum > self.targetSum or (currentSum + remainingSum) < self.targetSum or loc == self.N:
            return

        
        self.visited[loc] = True
        currentSum += self.weights[loc]
        remainingSum -= self.weights[loc]

        self.generateSubsetsUtil(loc+1, currentSum, remainingSum)

        self.visited[loc] = False
        currentSum -= self.weights[loc]

        self.generateSubsetsUtil(loc+1, currentSum, remainingSum)


    def printSubset(self):
        for i in range(self.N):
            if self.visited[i]:
                print(self.weights[i], end=', ')
        
        print(f"= {self.targetSum}")


if __name__ == '__main__':
    wt = [15, 22, 14, 26, 32, 9, 16, 8]
    targetSum = 53

    sol = Solution(wt, targetSum)
    sol.generateSubsets()