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

    def hasPathBfs(self,sv,ev):
        if ev>=self.n or ev<0:
            return None
        # make a visited array
        visited = [False for i in range(self.n)]
        # make a queue
        q = queue.Queue()
        q.put(sv)
        # make a parent dictionary
        parent = dict()
        # loop till queue is not empty
        while (not q.empty()):
            # implimenatation of queue
            val = q.get()
            # if base case come
            if val == ev:
                break
            # check for it's adjacent which is not visited yet
            for i in range(self.n):
                if (self.adjacentMatrix[val][i] > 0 and visited[i] is False):
                    q.put(i)
                    visited[i] = True
                    parent[i] = val

        # now it's time to print the answer via parent dictionary
        if ev in parent:
            ans = parent[ev]
            print(ev,end= " ")
            while ans!=sv:
                print(ans,end = " ")
                ans = parent[ans]
            print(sv)

    def __str__(self):
        return str(self.adjacentMatrix)



nVertices,nEdges = [int(ele) for ele in input().split()]
g = graph(nVertices)
for i in range(nEdges):
        v1,v2 = [int(ele) for ele in input().split()]
        g.addEdge(v1,v2)
x,y = [int(ele) for ele in input().split()]

g.hasPathBfs(x,y)