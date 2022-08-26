def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

def combination(n,m):
    return factorial(n)//factorial(n-m)//factorial(m)

def printPairDiffK(l, k):
    d = dict()
    count = 0
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1

    if k == 0:
        for i in l:
            count += combination(d[i],2)
            d[i] = 0
    else:
        for i in l:
            if (i-k) in d:
                count += min(d[i],d[i-k])
            if (i+k) in d:
                count += min(d[i],d[i+k])
            d[i] = 0
    
    return count 
        
    
# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
print(printPairDiffK(l, k))