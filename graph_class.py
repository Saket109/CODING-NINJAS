import queue

class graph:

    def __init__(self,n):
        self.n = n
        self.adjacentMatrix = [[0 for j in range(n)] for i in range(n)]

    def addEdge(self,v1,v2):
        self.adjacentMatrix[v1][v2] = 1
        self.adjacentMatrix[v2][v1] = 1

    def __dfsHelper(self,sv,visited):
        print(sv)
        visited[sv] = True
        for i in range(self.n):
            if (self.adjacentMatrix[sv][i] > 0 and visited[i] is False):
                self.__dfsHelper(i,visited)

    def dfs(self):
        visited = [False for i in range(self.n)]
        for i in range(self.n):
            if visited[i] is False:
                self.__dfsHelper(i,visited)

    def bfs(self):
        visited = [False for i in range(self.n)]
        q = queue.Queue()
        q.put(0)
        visited[0] = True
        while (not q.empty()):
            val = q.get()
            print(val,end = " ")
            for i in range(self.n):
                if (self.adjacentMatrix[val][i] > 0 and visited[i] is False):
                    q.put(i)
                    visited[i] = True


    def removeEdge(self,v1,v2):
        if self.containsEdge(v1,v2) is False:
            return
        self.adjacentMatrix[v1][v2] = 0
        self.adjacentMatrix[v2][v1] = 0

    def containsEdge(self,v1,v2):
        if self.adjacentMatrix[v1][v2] == 1:
            return True
        else:
            False

    def __str__(self):
        return str(self.adjacentMatrix)


# nVertices,nEdges = [int(ele) for ele in input().split()]
# if nEdges == 0:
#     for i in range(nVertices):
#         print(i,end=" ")
# else:
#     g = graph(nVertices)
#     for i in range(nEdges):
#         v1,v2 = [int(ele) for ele in input().split()]
#         g.addEdge(v1,v2)

#      g.bfs()

g = graph(6)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(2,3)
g.addEdge(2,4)
g.addEdge(4,5)
g.dfs()