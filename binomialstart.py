def combination(n,r):
    # print(factorial(n)//factorial(r)//factorial(n-r))
    return factorial(n)//factorial(r)//factorial(n-r)

def factorial(n):
    ans = 1
    for i in range(1,n+1):
        ans = ans*i
    return ans

row = int(input())


for i in range(1,row+1):
    k=1
    h=0
    for j in range(1,2*row):
        if (row+1)-i<=j and j<=(row-1)+i and k==1:
            if i == 1:
                print(i,end="")
            else:
                print(combination(i-1,h),end="")
                h+=1 
            k=0
        else:
            print(" ",end="")
            k=1
    print("\n")

