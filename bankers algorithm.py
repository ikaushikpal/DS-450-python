class BankerAlgo:
    def __init__(self, processes, resources):
        self.processes = processes
        self.resources = resources


    def setInitialState(self, available, maximum, allocation):
        self.available = available
        self.maximum = maximum
        self.allocation = allocation
        self.need = [[0] * self.resources for _ in range(self.processes)]

        for i in range(self.processes):
            for j in range(self.resources):
                self.need[i][j] = self.maximum[i][j] - self.allocation[i][j]


    def isSafe(self):
        work = self.available
        finish = [False] * self.processes
        safeSeq = []
        remainingProcesses = self.processes

        while remainingProcesses > 0:
            countProcesses = 0

            for i in range(self.processes):
                for j in range(self.resources):
                    if finish[i] == False and self.need[i][j] <= work[j]:
                        work[j] = work[j] + self.allocation[i][j]
                        finish[i] = True

                        safeSeq.append(i)

                        remainingProcesses -= 1
                        countProcesses += 1

            if countProcesses == 0:
                raise Exception("Unsafe State Detected")
        
        print(f"Safe Sequence = {safeSeq}")


    def request(self, process, requestedResource):
        for i in range(self.resources):
            if requestedResource[i] > self.need[process][i]:
                raise Exception(f"Process {process} has exceed its maximum claim")
            
            if requestedResource[i] > self.available[i]:
                print(f"Process {process} must wait")
                return
            
        for i in range(self.resources):
            self.available[i] -= requestedResource[i]
            self.allocation[process][i] += requestedResource[i]
            self.need[process][i] -= requestedResource[i]
        
        self.isSafe()


if __name__ == '__main__':
    banker = BankerAlgo(5, 3)
    banker.setInitialState([3, 3, 2], [[7, 5, 3],
                                       [3, 7, 2],
                                       [9, 0, 2],
                                       [2, 2, 2],
                                       [4, 3, 3],],[[0, 1, 0],
                                                    [2, 0, 0],
                                                    [3, 0, 2],
                                                    [2, 1, 1],
                                                    [0, 0, 2],])

    banker.isSafe()
    banker.request(1, [1, 7, 2])
