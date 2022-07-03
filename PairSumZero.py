from sys import stdin

def pairSum0(l,n):
    d = dict()
    count = 0

    for i in l:
        d[i] = d.get(i,0)+1
        if i == 0:
            pass
        
        elif -i in d:
            count+=(d[-i])
            
    
    if 0 in d:
        n = (d[0]*(d[0]-1))//2
        count+=n

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