class Solution:
    def printPath(self, cost, crossTime, enterTime, exitTime, line1, line2):
        if line1[0] + enterTime[0] < line2[0] + enterTime[1]:
            print(f'start {enterTime[0]} ->')
        else:
            print(f'start {enterTime[1]} ->')
            print()
    def assemblyLineScheduling(self, cost, crossTime, enterTime, exitTime):
        countStations = len(cost[0])
        line1 = [float('inf')] * countStations
        line2 = [float('inf')] * countStations

        line1[-1] = exitTime[0] + cost[0][-1]
        line2[-1] = exitTime[1] + cost[1][-1]

        for i in range(countStations-2, -1, -1):
            line1[i] = cost[0][i] + min(line1[i+1], line2[i+1] + crossTime[0][i+1])
            line2[i] = cost[1][i] + min(line2[i+1], line1[i+1] + crossTime[1][i+1])

        print(f'minimum cost = {min(line1[0] + enterTime[0], line2[0] + enterTime[1])}')
        self.printPath(cost, crossTime, enterTime, exitTime, line1, line2)
# Time Complexity: O(n)
# Space Complexity: O(n)


if __name__ == '__main__':
    sol = Solution()
    print(sol.assemblyLineScheduling(cost = [[4, 5, 3, 2],
                                        [2, 10, 1, 4]],
                                    crossTime = [[0, 7, 4, 5],
                                        [0, 9, 2, 8]],
                                    enterTime = [10, 12],
                                    exitTime = [18, 7]))
