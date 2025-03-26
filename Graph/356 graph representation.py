graph = [
        [0,1,0,1,1],
        [1,0,0,1,1],
        [0,1,0,1,1],
        [1,1,0,0,1],
        [1,1,0,1,0]
]

from collections import defaultdict

graph1 = defaultdict(list)
graph1[0] = [1,2,4]
graph1[1] = [0,2,4,3]
graph1[2] = []
graph1[3] = [1]
graph1[4] = [0]

