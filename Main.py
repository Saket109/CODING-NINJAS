# dynamic programming is like a recursion but here we will only deal with the case the 
    # subproblem is repeating itself.

def fibonacci(n,dp):
    if n == 1 or n == 0:
        return n
    if dp[n-1] == -1:
        ans1 = fibonacci(n-1,dp)
        dp[n-1] = ans1
    else:
        ans1 = dp[n-1]
    if dp[n-2] == -1 :
        ans2 = fibonacci(n-2,dp)
        dp[n-2] = ans2
    else:
        ans2 = dp[n-2]

    return ans1 + ans2

def fibbI(n):
    dp = [0 for i in range(n+1)]
    dp[0] = 0 
    dp[1] = 1
    i = 2
    while i<=n:
        dp[i] = dp[i-1] + dp[i-2]
        i+=1
    return dp[n]

n= int(input())
dp = [-1 for i in range(n+1)]
print(fibonacci(n,dp))
print(fibbI(n))