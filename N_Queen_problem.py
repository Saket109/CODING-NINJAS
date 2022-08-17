def safe(row,col,board):
    
    i = row-1
    while i>=0:
        if board[i][col] == 1:
            return False
        i-=1

    i = row-1
    j = col-1
    while i>=0 and j>=0:
        if board[i][j] == 1:
            return False
        i-=1
        j-=1

    i = row-1
    j = col+1
    while i>=0 and j<n:
        if board[i][j] == 1:
            return False
        i-=1
        j+=1

    return True

def nqueenhelper(n,board,x):
    # spedial case
    if x == n:
        for i in range(n):
            for j in range(n):
                print(board[i][j],end = " ")
        print()
        return
    
    for col in range(n):
        if safe(x,col,board):
            board[x][col] = 1
            nqueenhelper(n,board,x+1)
            board[x][col] = 0


    
    
def nQueen(n):
    board = [[0 for j in range(n)] for i in range(n)]
    nqueenhelper(n,board,0)


n = int(input())
nQueen(n)