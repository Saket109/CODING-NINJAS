def printmazehelper(x,y,maze,n,solution):
    # special case
    if x == n-1 and y == n-1 :
        solution[x][y] = 1
        print(solution)
        return
    # base case
    if x<0 or y<0 or x>=n or y>=n or maze[x][y] == 0 or solution[x][y] == 1:
        return 

    solution[x][y] = 1
    printmazehelper(x+1,y,maze,n,solution)
    printmazehelper(x,y+1,maze,n,solution)
    printmazehelper(x-1,y,maze,n,solution)
    printmazehelper(x,y-1,maze,n,solution)
    solution[x][y] = 0


def printmaze(maze):
    n = len(maze)
    solution = [[0 for j in range(n)] for i in range(n)]
    printmazehelper(0,0,maze,n,solution)

n=int(input())
maze=[]
for i in range(n):
    row=[int(ele) for ele in input().split()]
    maze.append(row)
    
printmaze(maze)