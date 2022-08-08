import sys,math

def minStepsTo1(n):
    dp = [-1 for i in range(n+1)]
    dp[0] = 0
    for i in range(1,n+1):
        root = int(math.sqrt(i))
        ans = sys.maxsize

        for j in range(1,root+1):
            ans = min(ans,dp[i-(j**2)])

        dp[i] = 1+ans

    return dp[n]


n = int(input())

ans = minStepsTo1(n)
print(ans)