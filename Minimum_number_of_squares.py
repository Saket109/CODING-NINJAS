# QUESTION : A number can always be represented as a sum of squares of other numbers. 
    # Note that 1 is a square and we can always break a number as 
        # [(1 * 1) + (1 * 1) + (1 * 1) + …]. Given a number n, find the 
            # minimum number of squares that sum to n.

import sys

def minStepsTo1(n,dp):
    if n == 0:
        return 0
    i = 1
    ans = n
    while i*i<=n:
        if dp[n-i*i] == -1:
            curr_ans = minStepsTo1(n-i*i,dp)
            dp[n-i*i] = curr_ans
        else:
            curr_ans = dp[n-i*i]

        ans = min(ans,curr_ans)
        i += 1
    
    return 1+ans

n = int(input())
dp = [-1 for i in range(n+1)]
ans = minStepsTo1(n,dp)
print(ans)
