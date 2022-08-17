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

    def __hasPathDfsHelper(self,v1,v2,visited):

        if v1 == v2:
            return [v2]

        visited[v1] = True
        
        for i in range(self.n):

            if self.adjacentMatrix[v1][i] > 0 and visited[i] is False:
                sol = self.__hasPathDfsHelper(i,v2,visited)

                if sol != None:
                    ans = sol
                    ans.append(v1)
                    return ans

                visited[i] = True

        return ans

    def hasPathDfs(self,v1,v2):
        if v2>=self.n or v2<0:
            return []
        visited = [False for i in range(self.n)]
        val = self.__hasPathDfsHelper(v1,v2,visited)
        if val == []:
            print()
        else:
            for i in val:
                print(i,end = " ")
        

    def __str__(self):
        return str(self.adjacentMatrix)



nVertices,nEdges = [int(ele) for ele in input().split()]
g = graph(nVertices)
for i in range(nEdges):
        v1,v2 = [int(ele) for ele in input().split()]
        g.addEdge(v1,v2)
x,y = [int(ele) for ele in input().split()]

g.hasPathDfs(x,y)