import queue

class graph:

    def __init__(self,n):
        self.n = n
        self.adjacentmatrix = [[0 for j in range(self.n)] for i in range(self.n)]

    def addEdge(self,v1,v2):
        self.adjacentmatrix[v1][v2] = 1
        self.adjacentmatrix[v2][v1] = 1

    def __connectedComponentsHelper(self,sv,visited,cc):
        visited[sv] = True
        for j in range(self.n):
                if (visited[j] is False and self.adjacentmatrix[sv][j] > 0):
                    cc.append(j)
                    visited[j] = True
                    self.__connectedComponentsHelper(j,visited,cc)

        return cc


    def connectedComponents(self):
        # make a visited array
        visited = [False for i in range(self.n)]

        # make a final list array
        finalList = []

        # check for every sv which is not visited yet
        for i in range(self.n):
            if visited[i] is False:
                cc = self.__connectedComponentsHelper(i,visited,[i])
                finalList.append(cc)

        return finalList

nVertices,nEdges = [int(ele) for ele in input().split()]
g = graph(nVertices)
for i in range(nEdges):
    v1,v2 = [int(ele) for ele in input().split()]
    g.addEdge(v1,v2)

ans = g.connectedComponents()
for i in ans:
    for j in i:
        print(j,end = " ")
    print()
