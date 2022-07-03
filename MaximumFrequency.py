from sys import stdin
def maxfreq(arr):
    if len(arr) == 0:
        return
    d = dict()
    ans = 0 

    for i in arr:
        d[i] = d.get(i,0)+1
        if ans == 0:
            ans = d[i]
        else:
            if ans < d[i]:
                ans = d[i]
         
    for i in arr:
        if d[i]==ans:
            ansreal = i 
            break
        
    return ansreal
    
    
    
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(maxfreq(arr))