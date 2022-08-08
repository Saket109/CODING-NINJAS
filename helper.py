from sys import stdin

def pairSum0(l,n):
    d = dict()
    count = 0

    for i in l:
        d[i] = d.get(i,0)+1

    for i in l:
        if i == 0:
            n = (d[i]*(d[i]-1))//2
            count+=n
            d[i]=0
        
        elif -i in d:
            count+=(d[i]*d[-i])
            d[i]=0

    return count


    
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(pairSum0(arr,n))