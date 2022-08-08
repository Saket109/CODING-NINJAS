# main
n = int(input())
i = 1
while(i<=n):
    k=1
    while (k<=n-i):
        print(" ",end = "")
        k+=1
    j =0
    while (j<2*i-1):
        print("*",end = "")
        j+=1
    i+=1
    print()