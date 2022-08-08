from sys import stdin
from sys import maxsize as MAX_VALUE


import sys
def countMinStepsToOne(n,dp) :
    dp[0] = 0
    dp[1] = 1
    i = 2 
    while i<=n:
        ans1 = dp[i-1]
        ans2 = sys.maxsize
        if i%2 == 0:
            ans2 = dp[i//2]
        ans3 = sys.maxsize
        if i%3 == 0:
            ans3 = dp[i//3]
        dp[i] = 1 + min(ans1,ans2,ans3)
        i += 1
        
    return dp[n]


#main
n = int(stdin.readline().rstrip())
dp = [-1 for i in range(n+1)]
print(countMinStepsToOne(n,dp))