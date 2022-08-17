from sys import stdin
import sys

def lcs(s,t) :
    dp = [[0 for i in range(len(t)+1)]for j in range(len(s)+1)]

    for i in range(len(s)-1,-1,-1):
        for j in range(len(t)-1,-1,-1):
            if s[i] == t[j]:
                ans = 1+dp[i+1][j+1]
            else:
                ans1 = dp[i+1][j]
                ans2 = dp[i][j+1]
                ans = max(ans1,ans2)

            dp[i][j] = ans

    return dp[0][0]

#main
s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())
print(lcs(s, t))