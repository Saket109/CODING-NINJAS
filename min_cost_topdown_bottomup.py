import sys

def minCostIterativeTD(cost,n,m):
    
    dp=[[sys.maxsize for j in range(m+1)]for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1 and j==1:
                dp[i][j]=cost[0][0]
            else:
                ans1=dp[i-1][j]
                ans2=dp[i][j-1]
                ans3=dp[i-1][j-1]
                dp[i][j]=cost[i-1][j-1]+min(ans1,ans2,ans3)
    return dp[n][m]
    
    
    
    
    
    
def minCostIterativeBU(cost,n,m):
    
    dp=[[sys.maxsize for j in range(m+1)]for i in range(n+1)]
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if i==n-1 and j==m-1:
                dp[i][j]=cost[i][j]
            else:
                ans1=dp[i+1][j]
                ans2=dp[i][j+1]
                ans3=dp[i+1][j+1]
                dp[i][j]=cost[i][j]+min(ans1,ans2,ans3)
    return dp[0][0]
cost=[[1,5,11],[8,13,12],[2,3,7],[15,16,18]]
n=4
m=3 
ans=minCostIterativeTD(cost,n,m)
print(ans)