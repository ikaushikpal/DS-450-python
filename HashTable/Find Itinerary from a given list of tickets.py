from collections import defaultdict, deque


class Solution1:
    def printIterary(self, pair):
        self.graph = defaultdict(list)
        for key, value in pair.items(): self.graph[key].append(value)

        self.topologicalSort()

    def dfs(self, vertex, visited, order):
        visited[vertex] = True

        for neighbour in self.graph[vertex]:

            if visited[neighbour] == False:
                self.dfs(neighbour, visited, order)

        order.append(vertex)

    def topologicalSort(self):
        visited = defaultdict(bool)
        order = deque()

        for vertex in list(self.graph):

            if visited[vertex] == False:
                self.dfs(vertex, visited, order)
        
        self.printOrder(order)

    
    def printOrder(self, order):
        print(' <- '.join(order))
        del order

# =============================================================
class Solution2:
    def printIterary(self, pair):
        originalSource = {}
        for key, value in pair.items():
            originalSource[value] = False

            if key in originalSource:
                originalSource[key] = False
            else:
                originalSource[key] = True

        # finding starting postion
        startLoc = None
        for loc in originalSource:
            if originalSource[loc] == True:
                startLoc = loc 
                break

        self.printOrder(startLoc, pair)


    def printOrder(self, currentLoc, pair):
        if currentLoc not in pair:
            print(f"{currentLoc}")
            
        else:
            print(f"{currentLoc} -> ",end='')
            self.printOrder(pair[currentLoc], pair)


if __name__ == '__main__':
    d = {}
    d["Chennai"] = "Banglore"
    d["Bombay"] = "Delhi"
    d["Goa"] = "Chennai"
    d["Delhi"] = "Goa"

    Solution1().printIterary(d)
    Solution2().printIterary(d)