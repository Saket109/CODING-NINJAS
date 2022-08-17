# QUESTION : Given two strings, 'S' and 'T' with lengths 'M' and 'N', find the length of the 
# 'Longest Common Subsequence'.For a string 'str'(per se) of length K, the subsequences 
# are the strings containing characters in the same relative order as they are present 
# in 'str,' but not necessarily contiguous. Subsequences contain all the strings of length 
# varying from 0 to K.


from sys import stdin
import sys

def lcs(s,t,i,j,dp) :
    # base case
    if i==len(s) or j==len(t):
        return 0

    # induction hypthosis
    if s[i] == t[j]:
        if dp[i+1][j+1] == -1:
            smallans = lcs(s,t,i+1,j+1,dp)
            dp[i+1][j+1] = smallans
            ans = 1+smallans
        else:
            ans = 1+dp[i+1][j+1]
    else:
        if dp[i+1][j] == -1:
            ans1 = lcs(s,t,i+1,j,dp)
            dp[i+1][j] = ans1
        else:
            ans1 = dp[i+1][j]

        if dp[i][j+1] == -1:
            ans2 = lcs(s,t,i,j+1,dp)
            dp[i][j+1] = ans2
        else:
            ans2 = dp[i][j+1]

        ans = max(ans1,ans2)

    return ans

#main
s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())
dp = [[-1 for i in range(len(s)+1)]for j in range(len(t)+1)]

print(lcs(s, t,0,0,dp))