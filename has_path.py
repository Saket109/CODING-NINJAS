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
        q.put(0)
        visited[0] = True
        while (not q.empty()):
            val = q.get()
            print(val,end = " ")
            for i in range(self.n):
                if (self.adjacentMatrix[val][i] > 0 and visited[i] is False):
                    q.put(i)
                    visited[i] = True

    def __hasPathHelper(self,v1,v2,visited):

        if self.adjacentMatrix[v1][v2] == 1:
            return True

        visited[v1] = True
        ans = False
        
        for i in range(self.n):
            if self.adjacentMatrix[i][v1] > 0 and visited[i] is False:
                ans = ans or self.__hasPathHelper(i,v2,visited)
                visited[i] = True
                if ans is True :
                    return True

        return False

    def hasPath(self,v1,v2):
        if v2>=self.n or v2<0:
            return False
        visited = [False for i in range(self.n)]
        val = self.__hasPathHelper(v1,v2,visited)
        return val
        

    def __str__(self):
        return str(self.adjacentMatrix)

nVertices,nEdges = [int(ele) for ele in input().split()]
g = graph(nVertices)
for i in range(nEdges):
        v1,v2 = [int(ele) for ele in input().split()]
        g.addEdge(v1,v2)
x,y = [int(ele) for ele in input().split()]
if g.hasPath(x,y):
    print("true")
else:
    print("false")