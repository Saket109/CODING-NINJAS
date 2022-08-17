import queue

class graph:

    def __init__(self,n):
        self.n = n
        self.adjacentMatrix = [[0 for j in range(n)] for i in range(n)]

    def addEdge(self,v1,v2):
        self.adjacentMatrix[v1][v2] = 1
        self.adjacentMatrix[v2][v1] = 1

    def bfs(self):
        visited = [False for i in range(self.n)]
        q = queue.Queue()
        for j in range(self.n):
            if visited[j] is False:
                q.put(j)
                visited[j] = True
                while (not q.empty()):
                    val = q.get()
                    print(val,end = " ")
                    for i in range(self.n):
                        if (self.adjacentMatrix[val][i] > 0 and visited[i] is False):
                            q.put(i)
                            visited[i] = True


    def __str__(self):
        return str(self.adjacentMatrix)


nVertices,nEdges = [int(ele) for ele in input().split()]
if nEdges == 0:
    for i in range(nVertices):
        print(i,end=" ")
else:
    g = graph(nVertices)
    for i in range(nEdges):
        v1,v2 = [int(ele) for ele in input().split()]
        g.addEdge(v1,v2)

    g.bfs()