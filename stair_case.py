def countStaircase(n):
    if n==0:
        return 1
    if n<0:
        return 0
    x=countStaircase(n-1)
    y=countStaircase(n-2)
    z=countStaircase(n-3)
    return x+y+z

n=int(input())
print(countStaircase(n))