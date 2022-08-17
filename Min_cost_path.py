# QUESTION : An integer matrix of size (M x N) has been given. Find out the minimum cost to 
# reach from the cell (0, 0) to (M - 1, N - 1).From a cell (i, j), you can move in three
#  directions:
# 1. ((i + 1),  j) which is, "down"
#2. (i, (j + 1)) which is, "to the right"
#3. ((i+1), (j+1)) which is, "to the diagonal"


from sys import stdin
MAX_VALUE = 2147483647

ans = 0
def minCostPath(input, mRows, nCols,i,j,dp) :
    global ans
    # special condition 
    if i==mRows-1 and j==nCols-1:
        return input[i][j]
    # base condition
    if i>=mRows or j>=nCols:
        return MAX_VALUE
    if i+1<mRows:
        if dp[i+1][j] == 0:
            val1 = minCostPath(input,mRows,nCols,i+1,j,dp)
            dp[i+1][j] = val1
        else:
            val1 = dp[i+1][j]
    else:
        val1 = minCostPath(input,mRows,nCols,i+1,j,dp)
    if j+1<nCols:
        if j+1 < nCols and dp[i][j+1] == 0:
            val2 = minCostPath(input,mRows,nCols,i,j+1,dp)
            dp[i][j+1] = val2
        else:
            val2 = dp[i][j+1]
    else:
        val2 = minCostPath(input,mRows,nCols,i,j+1,dp)
    if i+1<mRows and j+1<nCols:
        if i+1 < mRows and j+1 < nCols and dp[i+1][j+1] == 0:
            val3 = minCostPath(input,mRows,nCols,i+1,j+1,dp)
            dp[i+1][j+1] = val3
        else:
            val3 = dp[i+1][j+1]
    else:
        val3 = minCostPath(input,mRows,nCols,i+1,j+1,dp)

    result = min(val1,val2,val3)
    ans = input[i][j] + result

    return ans


#taking input using fast I/O method
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    mRows = int(li[0])
    nCols = int(li[1])
    
    if mRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(mRows)]
    return mat, mRows, nCols


#main
mat, mRows, nCols = take2DInput()
dp = [[0 for i in range(nCols)] for j in range(mRows)]
print(minCostPath(mat, mRows, nCols,0,0,dp))