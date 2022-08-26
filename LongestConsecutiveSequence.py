from sys import stdin

def first(arr,a,b):
    for i in range(len(arr)):
        if arr[i] == a:
            ans1 = i
    for j in range(len(arr)):
        if arr[j] == b:
            ans2 = j
    if ans1>ans2:
        return ans2
    else:
        return ans1


def longestConsecutiveSubsequence(arr,n): 
    d = dict()
    for i in arr:
        d[i]=True
    maxlength = 1
    end = arr[0]
    
    for i in arr:
        length = 0
        if d[i]:
            length += 1
            j = i
            while (j+1) in d:
                length+=1
                if length>maxlength:
                    maxlength = length
                    end = j+1
                d[j+1]=False
                j+=1
                if length == maxlength:
                    ans = first(arr,end-maxlength+1,j+1-maxlength)
                    end = ans+maxlength-1
            j=i
            while (j-1) in d:
                length+=1
                d[j-1]=False
                if length>maxlength:
                    maxlength = length
                    if i+1 not in d:
                        end = i
                # if length==maxlength:
                #     ans = first(arr,j-1,(end-maxlength+1))
                #     end = ans+maxlength-1
                j-=1
    if maxlength == 1:
        return end,end
    return end-maxlength+1,end


def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

    
# Main 
arr,n=takeInput()
ans = longestConsecutiveSubsequence(arr,n) 
# This ans array contains two numbers, ie, start and end of longest sequence respectively
print(*ans)