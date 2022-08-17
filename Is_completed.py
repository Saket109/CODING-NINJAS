# Write your code here
import queue

class graph:

    def __init__(self,n):
        self.n = n
        self.adjacentMatrix = [[0 for j in range(n)] for i in range(n)]

    def addEdge(self,v1,v2):
        self.adjacentMatrix[v1][v2] = 1
        self.adjacentMatrix[v2][v1] = 1

    def __isconnectedHelper(self,sv,visited):
        visited[sv] = True
        for i in range(self.n):
            if (self.adjacentMatrix[sv][i] > 0 and visited[i] is False):
                visited[i] = True
                self.__isconnectedHelper(i,visited)


    def isconnected(self,sv):
        # make a visited array
        visited = [False for i in range(self.n)]
        # make a helper function to use recursion (dfs)
        self.__isconnectedHelper(sv,visited)

        # now check the visited array to check connected graph 
        for i in range(self.n):
            if visited[i] is False:
                return False

        return True
        

    def __str__(self):
        return str(self.adjacentMatrix)



nVertices,nEdges = [int(ele) for ele in input().split()]
if nVertices == 0 or nVertices == 1:
    print("true")
else:
    g = graph(nVertices)
    for i in range(nEdges):
            v1,v2 = [int(ele) for ele in input().split()]
            g.addEdge(v1,v2)

    if g.isconnected(0):
        print("true")
    else:
        print("false")