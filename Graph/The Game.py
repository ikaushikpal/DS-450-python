from collections import deque


class Graph:
    def __init__(self, n, A):
        self.n = n
        self.graph = {x:[] for x in range(n)}
        self.A = A

    def addEdge(self, u, v):
        self.graph[u-1].append(v-1)
        
    def generate(self):
        queue = deque()

        for u in range(self.n):
            if self.A[u] == len(self.graph[u]):
                queue.append(u)
        
        return queue
    
    def game(self):
        queue = self.generate()
        if len(queue) == 0:
            return '0 -1'
        
        visited = [False] * self.n
        A_cpy = A.copy()
        score = maxx = 0

        while queue:
            u = queue.popleft()
            visited[u] = True

            for v in self.graph[u]:
                if visited[v] == False and A_cpy[u] > 0:
                    score += 1
                    A_cpy[v] += 1
                    A_cpy[u - 1] -= 1

                    if A_cpy[v] == len(self.graph[v]):
                        queue.append(v)
        
        for i in range(self.n):
            if visited[i] == False:
                maxx += max(0, len(self.graph[i]) - self.A[i])
        
        if maxx == 0:
            return f'{score} -1'
        return f'{score} {maxx}'
                    


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    g = Graph(n, A)
    for _ in range(m):
        u, v = map(int, input().split())
        g.addEdge(u, v)
    
    print(g.game())