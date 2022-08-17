# here instead of returning the answer , we are interested in printing the answer.
# thus after every step we will store and update our result and finally at the base case we 
# will print the answer and return.

def printfact(n,ans):
    if n == 0:
        print(ans)
        return
    ans = n*ans
    printfact(n-1,ans)

n = int(input())
printfact(n,1)