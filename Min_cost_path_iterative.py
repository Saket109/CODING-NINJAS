
from sys import stdin
MAX_VALUE = 2147483647

def minCostPath(input, mRows, nCols) :
    dp = [[0 for _ in range(nCols)] for _ in range(mRows)]
    dp[mRows-1][nCols-1] = input[mRows-1][nCols-1]

    for i in range(mRows-1,-1,-1):
        for j in range(nCols-1,-1,-1):
            if i+1==mRows and j+1==nCols:
                pass
            else:
                if i+1 == mRows:
                    val1 = MAX_VALUE
                else:
                    val1 = dp[i+1][j]
                if j+1 == nCols:
                    val2 = MAX_VALUE
                else:
                    val2 = dp[i][j+1]
                if i+1==mRows or j+1==nCols:
                    val3 = MAX_VALUE
                else:
                    val3 = dp[i+1][j+1]
                result = min(val1,val2,val3)
                ans = input[i][j] + result
                dp[i][j] = ans
    
    return dp[0][0]





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
print(minCostPath(mat, mRows, nCols))