def findbit(n,i):
    x = 1<<(i-1)
    ans = n&x
    return ans 

n = int(input())
i = int(input())
if findbit(n,i):
    print(1)
else:
    print(0)

